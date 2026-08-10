#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

echo ">>> Compiling C++ SIMD vector matching engine..."

# Ensure we are in the project root
cd "$(dirname "$0")/.."

# Create and enter the build directory
mkdir -p build
cd build

# Configure CMake, explicitly targeting Python 3.11 for the Pybind11 wrapper
echo ">>> Running CMake configuration..."
cmake -DPYTHON_EXECUTABLE=$(which python3.11) ..

# Compile using all available CPU cores
echo ">>> Executing Make..."
make -j$(nproc)

# Move the compiled shared object (.so for Linux/Mac, .pyd for Windows) into the core directory
echo ">>> Relocating compiled library to core module..."
cp fast_matcher*.so ../core/ 2>/dev/null || cp fast_matcher*.pyd ../core/ 2>/dev/null

echo ">>> Compilation successful. The 'fast_matcher' engine is ready."
