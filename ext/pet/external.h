// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved

// code guard
#pragma once


// STL
#include <string>

// journal
#include <pyre/journal.h>


// pybind support
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>


// type aliases
namespace pet::py {
    // import {pybind11}
    namespace py = pybind11;
    // get the special {pybind11} literals
    using namespace py::literals;

    // sizes of things
    using size_t = std::size_t;
    // strings
    using string_t = std::string;
} // namespace pet::py


// end of file
