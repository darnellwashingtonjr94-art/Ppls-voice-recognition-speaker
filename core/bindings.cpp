#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "vector_engine.cpp"

namespace py = pybind11;

PYBIND11_MODULE(fast_matcher, m) {
    m.doc() = "High-performance SIMD vector matching engine";

    py::class_<VectorEngine>(m, "VectorEngine")
        .def(py::init<>())
        .def("compute_cosine_simd", &VectorEngine::compute_cosine_simd, 
             "Compute cosine similarity against a database matrix");
}
