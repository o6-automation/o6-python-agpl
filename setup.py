from dataclasses import dataclass
from setuptools import setup, Extension, Command, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
import os
import shlex
import subprocess
import sys
import numpy

# Check Python version requirement
if not (3, 11) <= sys.version_info[:2] < (3, 15):
    print("Error: This package requires Python 3.11 through 3.14.", file=sys.stderr)
    print(
        f"You are using Python {sys.version_info.major}.{sys.version_info.minor}.",
        file=sys.stderr,
    )
    sys.exit(1)

# Check NumPy version requirement (NPY_VSTRING and other APIs require NumPy 2.0+)
from packaging.version import Version

if not Version("2.0") <= Version(numpy.__version__) < Version("3"):
    print("Error: This package requires NumPy 2.x.", file=sys.stderr)
    print(
        f"You have NumPy {numpy.__version__}. Run: pip install 'numpy>=2,<3'",
        file=sys.stderr,
    )
    sys.exit(1)

# By default open62541 is built locally and linked statically into the extension.
# Set O6_USE_SYSTEM_LIB=1 to skip the local build and rely on the system-installed library.
BUNDLED_O6 = not bool(os.environ.get("O6_USE_SYSTEM_LIB", "").strip("0 "))

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def project_path(*parts):
    return os.path.join(ROOT_DIR, *parts)


def windows_arch():
    # cibuildwheel sets this for cross-compiled Windows ARM64 wheels. The
    # build interpreter itself remains AMD64, so pointer size is insufficient.
    target = os.environ.get("VSCMD_ARG_TGT_ARCH", "").lower()
    if target in {"arm64", "x64", "x86"}:
        return target

    import platform

    machine = platform.machine().lower()
    if machine in {"arm64", "aarch64"}:
        return "arm64"
    return "x64" if sys.maxsize > 2**32 else "x86"


@dataclass(frozen=True)
class BuildConfig:
    bundled_o6: bool
    platform: str

    @property
    def is_windows(self):
        return self.platform == "win32"

    @property
    def bundled_build_dir(self):
        if self.is_windows:
            return project_path("deps", "open62541", f"build-{windows_arch()}")
        return project_path("deps", "open62541", "build")

    @property
    def bundled_install_dir(self):
        return os.path.join(self.bundled_build_dir, "install")

    @property
    def bundled_lib_dir(self):
        return os.path.join(self.bundled_install_dir, "lib")

    @property
    def bundled_include_dir(self):
        return os.path.join(self.bundled_install_dir, "include")

    @property
    def bundled_generated_dir(self):
        return os.path.join(self.bundled_build_dir, "src_generated")

    @property
    def bundled_static_lib(self):
        filename = "open62541.lib" if self.is_windows else "libopen62541.a"
        return os.path.join(self.bundled_lib_dir, filename)

    @property
    def bundled_pkg_config_dir(self):
        return os.path.join(self.bundled_lib_dir, "pkgconfig")

    @property
    def windows_dependency_dir(self):
        if not self.is_windows:
            return None
        vcpkg_root = os.environ.get("VCPKG_ROOT", r"C:\vcpkg")
        return os.path.join(vcpkg_root, "installed", f"{windows_arch()}-windows-static")

    @property
    def schema_candidates(self):
        return [
            os.path.join(self.bundled_install_dir, "share", "open62541", "schema"),
            os.path.join("/usr", "local", "share", "open62541", "schema"),
            os.path.join("/usr", "share", "open62541", "schema"),
        ]


CONFIG = BuildConfig(
    bundled_o6=BUNDLED_O6,
    platform=sys.platform,
)


def source_files(config):
    sources = [
        "src/module.c",
        "src/types.c",
        "src/types_builtin.c",
        "src/types_struct.c",
        "src/types_convert.c",
        "src/types_common.c",
        "src/types_datavalue.c",
        "src/types_diagnosticinfo.c",
        "src/types_encoding.c",
        "src/types_mapping.c",
        "src/type_registration.c",
        "src/datatypes.c",
        "src/utils.c",
        "src/ua_extension_namespacemapping.c",
        "src/client/client.c",
        "src/client/client_config.c",
        "src/client/client_services.c",
        "src/client/client_services_subscriptions.c",
        "src/client/client_services_util.c",
        "src/logger.c",
        "src/eventloop/eventloop.c",
        "src/eventloop/eventloop_tcp.c",
        "src/eventloop/eventloop_udp.c",
        "src/eventloop/eventloop_ethernet.c",
        "src/bootstrap_ns0_types.c",  # Hand-maintained StatusCode + _Enum metaclass
        "src/init_pro.c",
        "src/services_subscriptions.c",
        "deps/tweetnacl/tweetnacl.c",
        "src/server/server.c",
        "src/server/server_access_control.c",
        "src/server/server_config.c",
        "src/server/server_events.c",
        "src/server/python_nodestore.c",
        "src/server/server_nodes.c",
        "src/server/server_pubsub.c",
        "src/server/server_rbac.c",
        "src/server/server_services.c",
        "src/server/server_services_subscriptions.c",
        "src/server/server_services_util.c",
    ]
    return sources


def include_dirs(config):
    dirs = [
        numpy.get_include(),
        project_path("src"),
        project_path("src", "client"),
        project_path("deps", "tweetnacl"),
        # open62541 internal headers (needed by src/client/client_extensions.c
        # for direct access to UA_Client and UA_NamespaceMapping internals).
        project_path("deps", "open62541", "src"),
        project_path("deps", "open62541", "src", "client"),
        project_path("deps", "open62541", "deps"),
        config.bundled_generated_dir,
        project_path("src", "server"),
    ]
    if config.bundled_o6:
        dirs.append(config.bundled_include_dir)
    return dirs


def make_extension(config):
    development_compile_args = []
    if not os.environ.get("CIBUILDWHEEL"):
        development_compile_args = ["/Od", "/Zi"] if config.is_windows else ["-O0", "-g"]
    return Extension(
        "o6._o6",
        sources=source_files(config),
        libraries=[] if config.bundled_o6 else ["open62541"],
        library_dirs=[] if config.bundled_o6 else [config.bundled_lib_dir],
        extra_objects=[config.bundled_static_lib] if config.bundled_o6 else [],
        extra_compile_args=development_compile_args,
        extra_link_args=[],
        undef_macros=["NDEBUG"],
        include_dirs=include_dirs(config),
    )


o6_core = make_extension(CONFIG)


# Setup function
class build_open62541(Command):
    """Clone and build open62541 into deps/open62541/build/install if not already present."""

    description = "clone/init and build open62541 into deps/open62541/build/install"
    user_options = [
        (
            "open62541-ref=",
            None,
            "git ref to checkout (default: HEAD of default branch)",
        ),
    ]

    _CLONE_DIR = project_path("deps", "open62541")

    def initialize_options(self):
        self.open62541_ref = None

    def finalize_options(self):
        pass

    def run(self):
        src = self._CLONE_DIR
        build_dir = CONFIG.bundled_build_dir
        install_dir = CONFIG.bundled_install_dir

        if not os.path.isfile(os.path.join(src, "CMakeLists.txt")):
            raise RuntimeError(
                "[open62541] deps/open62541 must already be present as a checked-out submodule. "
                "Run: git submodule update --init --recursive deps/open62541"
            )

        print(f"[open62541] using existing source tree at {src}")

        print(f"[open62541] configuring ...")
        cmake_args = [
            "cmake",
            "-B",
            build_dir,
            "-DBUILD_SHARED_LIBS=OFF",
            "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
            f"-DCMAKE_BUILD_TYPE={'Release' if os.environ.get('CIBUILDWHEEL') else 'Debug'}",
            "-DUA_ENABLE_DEBUG_SANITIZER=OFF",
            "-DUA_ENABLE_TOOLS=ON",
            "-DUA_ENABLE_QUERY=ON",
            "-DUA_ENABLE_RBAC=ON",
            "-DUA_ENABLE_DISCOVERY=ON",
            "-DUA_ENABLE_ENCRYPTION=OPENSSL",
            "-DUA_ENABLE_MQTT=ON",
            "-DUA_NAMESPACE_ZERO=FULL",
            "-DCMAKE_INSTALL_LIBDIR=lib",  # AlmaLinux/RHEL default is lib64; force lib for portability
            f"-DCMAKE_INSTALL_PREFIX={install_dir}",
        ]
        if CONFIG.is_windows:
            dependency_dir = CONFIG.windows_dependency_dir
            cmake_args.extend(
                [
                    "-A",
                    "ARM64" if windows_arch() == "arm64" else "x64",
                    f"-DCMAKE_PREFIX_PATH={dependency_dir}",
                    f"-DOPENSSL_ROOT_DIR={dependency_dir}",
                    "-DOPENSSL_USE_STATIC_LIBS=TRUE",
                ]
            )
        subprocess.check_call(cmake_args, cwd=src)

        cpu_count = str(os.cpu_count() or 1)
        print(f"[open62541] building ...")
        subprocess.check_call(["cmake", "--build", build_dir, f"-j{cpu_count}"])

        print(f"[open62541] installing into {install_dir} ...")
        subprocess.check_call(["cmake", "--install", build_dir])
        print(f"[open62541] done")


class build_ext(_build_ext):
    """Custom build_ext that optionally builds open62541 before linking the extension."""

    @staticmethod
    def _bundled_pkg_config_dir():
        return CONFIG.bundled_pkg_config_dir

    @classmethod
    def _bundled_static_link_args(cls):
        pkg_config_dir = cls._bundled_pkg_config_dir()
        env = os.environ.copy()
        existing = env.get("PKG_CONFIG_PATH", "")
        env["PKG_CONFIG_PATH"] = (
            pkg_config_dir if not existing else pkg_config_dir + os.pathsep + existing
        )

        try:
            output = subprocess.check_output(
                ["pkg-config", "--libs", "--static", "open62541"],
                env=env,
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            # The bundled open62541 install does not currently install an
            # open62541.pc file. It is configured above with the OpenSSL
            # backend, so its static archive leaves OpenSSL symbols for the
            # final extension link to resolve explicitly.
            try:
                output = subprocess.check_output(
                    ["pkg-config", "--libs", "--static", "openssl"],
                    stderr=subprocess.DEVNULL,
                    text=True,
                ).strip()
            except (subprocess.CalledProcessError, FileNotFoundError):
                return []

        lib_dir = CONFIG.bundled_lib_dir
        return [
            token for token in shlex.split(output) if token not in ("-lopen62541", f"-L{lib_dir}")
        ]

    def _configure_bundled_static_linkage(self):
        bundled_static_lib = CONFIG.bundled_static_lib
        if not os.path.isfile(bundled_static_lib):
            raise RuntimeError(f"[open62541] static library not found: {bundled_static_lib}")

        link_args = self._bundled_static_link_args()
        for ext in self.extensions:
            if CONFIG.is_windows:
                ext.libraries = [
                    "libssl",
                    "libcrypto",
                    "crypt32",
                    "bcrypt",
                    "ws2_32",
                    "iphlpapi",
                    "advapi32",
                    "user32",
                ]
                ext.library_dirs = [os.path.join(CONFIG.windows_dependency_dir, "lib")]
            else:
                ext.libraries = []
                ext.library_dirs = []
            ext.extra_objects = [bundled_static_lib]
            ext.extra_link_args = list(ext.extra_link_args) + link_args

    def run(self):
        if BUNDLED_O6:
            self.run_command("build_open62541")
            self._configure_bundled_static_linkage()
        super().run()


setup(
    name="o6",
    version="2.0.1",
    ext_modules=[o6_core],
    cmdclass={
        "build_ext": build_ext,
        "build_open62541": build_open62541,
    },
    packages=find_packages(exclude=["tests*", "build*", "deps*", "tools*"]),
    #    test_suite="tests",  # Directory for test discovery (pytest)
)
