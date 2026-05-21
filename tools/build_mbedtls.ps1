$ErrorActionPreference = 'Stop'

# Detect target architecture from the Python interpreter cibuildwheel is using.
# This is the only reliable source when VSCMD_ARG_TGT_ARCH is not yet set.
$pyArch = & python -c "import struct; print('x64' if struct.calcsize('P') == 8 else 'x86')"
Write-Host "[mbedtls] target arch: $pyArch"

$base   = Join-Path $env:LOCALAPPDATA 'mbedtls'
$prefix = "${base}-${pyArch}"

if (Test-Path $prefix) {
    Write-Host "[mbedtls] already installed at $prefix, skipping"
    exit 0
}

$v       = '3.6.3'
$srcDir  = "${base}-src"
$tarball = "${base}-src.tar.gz"

if (-not (Test-Path (Join-Path $srcDir "mbedtls-$v"))) {
    Write-Host "[mbedtls] downloading mbedtls $v ..."
    Invoke-WebRequest "https://github.com/Mbed-TLS/mbedtls/archive/refs/tags/v${v}.tar.gz" -OutFile $tarball
    New-Item -Force -ItemType Directory $srcDir | Out-Null
    tar xzf $tarball -C $srcDir
}

# Locate vswhere.exe — ships with VS installer but may be in different places.
# Store ProgramFiles(x86) first; the parentheses cause issues inside array literals.
$pf86 = ${env:ProgramFiles(x86)}
$vswhereCandidates = @(
    (Join-Path $pf86            'Microsoft Visual Studio\Installer\vswhere.exe'),
    (Join-Path $env:ProgramFiles 'Microsoft Visual Studio\Installer\vswhere.exe'),
    (Join-Path $pf86            'Microsoft Visual Studio\2022\BuildTools\Common7\Tools\vswhere.exe'),
    (Join-Path $pf86            'Microsoft Visual Studio\2019\BuildTools\Common7\Tools\vswhere.exe')
)
$vswhere = $vswhereCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $vswhere) {
    # PS 5.1-compatible fallback (?.Source requires PS 7+)
    $cmd = Get-Command vswhere.exe -ErrorAction SilentlyContinue
    if ($cmd) { $vswhere = $cmd.Source }
}
if (-not $vswhere) {
    Write-Error "[mbedtls] vswhere.exe not found. Install Visual Studio Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/) with the 'Desktop development with C++' workload."
    exit 1
}
Write-Host "[mbedtls] using vswhere: $vswhere"
$vsPath    = (& $vswhere -latest -products * -property installationPath).Trim()
if (-not $vsPath) {
    Write-Error "[mbedtls] No Visual Studio or Build Tools installation found. Install Visual Studio Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/) with the 'Desktop development with C++' workload."
    exit 1
}
$vcvarsall = Join-Path $vsPath 'VC\Auxiliary\Build\vcvarsall.bat'

$buildDir = "${base}-build-${pyArch}"
$src      = Join-Path $srcDir "mbedtls-$v"

Write-Host "[mbedtls] configuring + building for $pyArch ..."

# Write a temp .bat file to avoid cmd.exe quoting issues with spaces in paths.
$batContent = "@echo off`r`n" +
              "call `"$vcvarsall`" $pyArch`r`n" +
              "if errorlevel 1 exit /b 1`r`n" +
              "cmake -G Ninja -B `"$buildDir`" -S `"$src`" -DCMAKE_BUILD_TYPE=Release -DENABLE_TESTING=OFF -DENABLE_PROGRAMS=OFF -DBUILD_SHARED_LIBS=OFF`r`n" +
              "if errorlevel 1 exit /b 1`r`n" +
              "cmake --build `"$buildDir`"`r`n" +
              "if errorlevel 1 exit /b 1`r`n" +
              "cmake --install `"$buildDir`" --prefix `"$prefix`"`r`n"
$batFile = [System.IO.Path]::GetTempFileName() + ".bat"
[System.IO.File]::WriteAllText($batFile, $batContent)
try {
    & cmd /c $batFile
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
    Remove-Item $batFile -ErrorAction SilentlyContinue
}

Write-Host "[mbedtls] installed to $prefix"
