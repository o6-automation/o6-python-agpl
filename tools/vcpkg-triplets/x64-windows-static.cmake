set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE static)
set(VCPKG_LIBRARY_LINKAGE static)

# Overlay of vcpkg's stock x64-windows-static triplet: we only ever link the
# Release build (setup.py never uses the debug OpenSSL libs), so skip
# building the debug variant entirely -- halves the OpenSSL build time on a
# cache miss.
set(VCPKG_BUILD_TYPE release)
