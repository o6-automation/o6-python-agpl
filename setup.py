from setuptools import setup, Extension, Command, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize
import os
import shutil
import subprocess
import sys
import numpy

# Check Python version requirement
if sys.version_info < (3, 11):
    print("Error: This package requires Python 3.11 or higher.", file=sys.stderr)
    print(
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}.",
        file=sys.stderr,
    )
    sys.exit(1)

# Check NumPy version requirement (NPY_VSTRING and other APIs require NumPy 2.0+)
from packaging.version import Version

if Version(numpy.__version__) < Version("2.0"):
    print(f"Error: This package requires NumPy 2.0 or higher.", file=sys.stderr)
    print(
        f"You have NumPy {numpy.__version__}. Run: pip install 'numpy>=2.0'",
        file=sys.stderr,
    )
    sys.exit(1)

# By default open62541 is built locally and bundled with the extension.
# Set O6_USE_SYSTEM_LIB=1 to skip the local build and rely on the system-installed library.
BUNDLED_O6 = not bool(os.environ.get("O6_USE_SYSTEM_LIB", "").strip("0 "))

# Set O6_NO_SERVER=1 to exclude server code from the build.
NO_SERVER = bool(os.environ.get("O6_NO_SERVER", "").strip("0 "))

_BUNDLED_INSTALL_DIR = os.path.join("deps", "open62541", "build", "install")

_library_dirs = [os.path.join(_BUNDLED_INSTALL_DIR, "lib")] if BUNDLED_O6 else []
_include_dirs = [
    numpy.get_include(),
    "src",
    "src/client",
    "deps",
]
if not NO_SERVER:
    _include_dirs.append("src/server")
if BUNDLED_O6:
    _include_dirs.append(os.path.join(_BUNDLED_INSTALL_DIR, "include"))

# Bundle the .so next to the extension only when building from a local install
_extra_link_args = ["-Wl,-rpath,$ORIGIN"] if BUNDLED_O6 else []

_define_macros = []
if NO_SERVER:
    _define_macros.append(("O6_NO_SERVER", "1"))

AGPL = False

src_files = [
    "src/init.c",
    "src/module.c",
    "src/types.c",
    "src/types_builtin.c",
    "src/types_struct.c",
    "src/types_convert.c",
    "src/types_common.c",
    "src/types_datavalue.c",
    "src/types_encoding.c",
    "src/type_registration.c",
    "src/utils.c",
    "src/client/client.c",
    "src/client/client_config.c",
    "src/client/client_services.c",
    "src/client/type_registration.c",
    "src/client/client_services_subscriptions.c",
    "src/client/client_services_util.c",
    "src/logger.c",
    "src/eventloop/eventloop.c",
    "src/eventloop/eventloop_tcp.c",
    "deps/eventloop_common.c",
    "src_gen/src_cmodule_enum.c",  # Generated enums
]

if not NO_SERVER:
    src_files += [
        "src/server/server.c",
        "src/server/server_config.c",
        "src/server/server_nodes.c",
        "src/server/type_registration.c",
    ]

# Define the extension module
o6_core = Extension(
    "o6._o6",  # Name of the extension module
    sources=src_files,
    libraries=["open62541"],  # Libraries to link against
    library_dirs=_library_dirs,
    extra_compile_args=["-O0", "-g"],  # No optimization, include debug info
    extra_link_args=_extra_link_args,
    define_macros=_define_macros,
    undef_macros=["NDEBUG"],  # This removes -DNDEBUG
    include_dirs=_include_dirs,
)


# Setup function
class build_open62541(Command):
    """Clone and build open62541 into deps/open62541/build/install if not already present."""

    description = "build and install open62541 into deps/open62541/build/install"
    user_options = [
        (
            "open62541-ref=",
            None,
            "git ref to checkout (default: HEAD of default branch)",
        ),
    ]

    _REPO = "https://github.com/open62541/open62541.git"
    _CLONE_DIR = os.path.join("deps", "open62541")

    def initialize_options(self):
        self.open62541_ref = None

    def finalize_options(self):
        pass

    def run(self):
        src = self._CLONE_DIR
        install_dir = os.path.abspath(os.path.join(src, "build", "install"))
        marker = os.path.join(install_dir, "lib", "libopen62541.so")
        if os.path.exists(marker):
            print(f"open62541 already installed at {install_dir}, skipping build")
            return
        if not os.path.isdir(src):
            print(f"[open62541] cloning into {src} ...")
            cmd = ["git", "clone", "--depth", "1"]
            if self.open62541_ref:
                cmd += ["--branch", self.open62541_ref]
            cmd += [self._REPO, src]
            subprocess.check_call(cmd)
        else:
            print(f"[open62541] using existing source tree at {src}")

        patch = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "open62541-client-namespace-mapping.patch",
        )
        if (
            subprocess.run(
                ["git", "apply", "--reverse", "--check", patch],
                cwd=os.path.abspath(src),
                capture_output=True,
            ).returncode
            != 0
        ):
            print(f"[open62541] applying namespace mapping patch")
            subprocess.check_call(["git", "apply", patch], cwd=os.path.abspath(src))

        build_dir = os.path.abspath(os.path.join(src, "build"))
        print(f"[open62541] configuring ...")
        subprocess.check_call(
            [
                "cmake",
                "-B",
                build_dir,
                "-DBUILD_SHARED_LIBS=ON",
                "-DCMAKE_BUILD_TYPE=Debug",
                "-DUA_ENABLE_TOOLS=ON",
                "-DUA_ENABLE_QUERY=ON",
                "-DUA_ENABLE_ENCRYPTION=MBEDTLS",
                f"-DCMAKE_INSTALL_PREFIX={install_dir}",
            ],
            cwd=src,
        )

        cpu_count = str(os.cpu_count() or 1)
        print(f"[open62541] building ...")
        subprocess.check_call(["cmake", "--build", build_dir, f"-j{cpu_count}"])

        print(f"[open62541] installing into {install_dir} ...")
        subprocess.check_call(["cmake", "--install", build_dir])
        print(f"[open62541] done")


class src_gen(Command):
    """Generate C enum sources from an OPC UA NodeSet2 XML file."""

    description = "generate src_gen/ sources (enums + node ids)"
    user_options = [
        (
            "nodeset=",
            None,
            "path to the NodeSet2 XML file (default: tools/merged_opcua_enum_nodeset2.xml)",
        ),
    ]

    _OUTPUT_DIR = "src_gen"
    _DEFAULT_NODESET = os.path.join("tools", "merged_opcua_enum_nodeset2.xml")
    _ENUM_GENERATOR = os.path.join("tools", "generate_python_enums.py")
    _DATATYPES_GENERATOR = os.path.join("tools", "generate_python_datatypes.py")
    _TYPES_GEN_PYI = os.path.join("o6", "_o6", "types_gen.pyi")
    _NODEIDS_CSV = os.path.join("tools", "NodeIds.csv")

    _SCHEMA_CANDIDATES = [
        # Bundled build
        os.path.join(
            "deps", "open62541", "build", "install", "share", "open62541", "schema"
        ),
        # Common system-install prefixes
        os.path.join("/usr", "local", "share", "open62541", "schema"),
        os.path.join("/usr", "share", "open62541", "schema"),
    ]

    @staticmethod
    def _find_schema_dir() -> "str | None":
        """Return the first schema directory that contains the required files, or None."""
        candidates = list(src_gen._SCHEMA_CANDIDATES)
        # Also try the prefix reported by pkg-config
        try:
            prefix = subprocess.check_output(
                ["pkg-config", "--variable=prefix", "open62541"],
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
            if prefix:
                candidates.insert(
                    0, os.path.join(prefix, "share", "open62541", "schema")
                )
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        for d in candidates:
            if os.path.isfile(os.path.join(d, "Opc.Ua.Types.bsd")) and os.path.isfile(
                os.path.join(d, "NodeIds.csv")
            ):
                return d
        return None

    def initialize_options(self):
        self.nodeset = None

    def finalize_options(self):
        if self.nodeset is None:
            self.nodeset = self._DEFAULT_NODESET

    def run(self):
        os.makedirs(self._OUTPUT_DIR, exist_ok=True)
        print(
            f"[src_gen] generating enum sources from {self.nodeset} into {self._OUTPUT_DIR}/"
        )
        subprocess.check_call(
            [sys.executable, self._ENUM_GENERATOR, self.nodeset, self._OUTPUT_DIR]
        )
        schema = self._find_schema_dir()
        if schema is not None:
            # Prefer local NodeIds.csv if the schema one is not readable
            schema_csv = os.path.join(schema, "NodeIds.csv")
            if not os.access(schema_csv, os.R_OK):
                schema_csv = self._NODEIDS_CSV
            print(f"[src_gen] generating OPC UA type stubs into {self._TYPES_GEN_PYI}")
            subprocess.check_call(
                [
                    sys.executable,
                    self._DATATYPES_GENERATOR,
                    "-t",
                    os.path.join(schema, "Opc.Ua.Types.bsd"),
                    "-c",
                    schema_csv,
                    "-n",
                    self.nodeset,
                    "-o",
                    self._TYPES_GEN_PYI,
                ]
            )
        else:
            print(
                f"[src_gen] skipping types_gen.pyi: open62541 schema not found "
                f"(checked: {', '.join(self._SCHEMA_CANDIDATES)} and pkg-config)"
            )


class build_ext(_build_ext):
    """Custom build_ext that optionally builds open62541 and bundles it alongside the extension."""

    _SONAME = "libopen62541.so.1.5"

    @staticmethod
    def _find_bundled_lib():
        """Return the path to the versioned libopen62541.so.*.*.* in the bundled install dir, or None."""
        import glob

        lib_dir = os.path.join(_BUNDLED_INSTALL_DIR, "lib")
        matches = glob.glob(os.path.join(lib_dir, "libopen62541.so.*.*.*"))
        return matches[0] if matches else None

    def run(self):
        self.run_command("src_gen")
        if BUNDLED_O6 and not self._find_bundled_lib():
            self.run_command("build_open62541")
        super().run()
        self._bundle_shared_lib()

    def copy_extensions_to_source(self):
        """Also bundle when copying to source dir (editable installs)."""
        super().copy_extensions_to_source()
        self._bundle_shared_lib(use_inplace=True)

    def _bundle_shared_lib(self, use_inplace=False):
        bundled_lib = self._find_bundled_lib()
        if bundled_lib is None:
            print(
                f"skipping bundling: libopen62541 not found in {_BUNDLED_INSTALL_DIR}/lib (using system-installed library)"
            )
            return
        for ext in self.extensions:
            ext_path = (
                self.get_ext_fullpath(ext.name)
                if not use_inplace
                else os.path.join(
                    self.get_finalized_command("build_py").get_package_dir(
                        ".".join(ext.name.split(".")[:-1]) or ""
                    ),
                    os.path.basename(self.get_ext_fullpath(ext.name)),
                )
            )
            dest_dir = os.path.dirname(os.path.abspath(ext_path))
            os.makedirs(dest_dir, exist_ok=True)

            # Copy versioned .so
            versioned_dest = os.path.join(dest_dir, os.path.basename(bundled_lib))
            shutil.copy2(bundled_lib, versioned_dest)
            print(f"bundled {versioned_dest}")

            # Create SONAME symlink
            soname_link = os.path.join(dest_dir, self._SONAME)
            if os.path.lexists(soname_link):
                os.remove(soname_link)
            os.symlink(os.path.basename(bundled_lib), soname_link)
            print(f"symlink  {soname_link} -> {os.path.basename(bundled_lib)}")


setup(
    name="o6",
    version="0.01",
    ext_modules=[o6_core],
    cmdclass={
        "build_ext": build_ext,
        "build_open62541": build_open62541,
        "src_gen": src_gen,
    },
    package_data={
        "": ["libopen62541.so.*", "libopen62541.so"],
    },
    packages=find_packages(exclude=["tests*", "build*", "deps*", "tools*"]),
    #    test_suite="tests",  # Directory for test discovery (pytest)
)
