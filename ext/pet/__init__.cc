// -*- C++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// declarations
#include "__init__.h"


// the module entry point
PYBIND11_MODULE(pet, m)
{
    // the doc string
    m.doc() = "the libpet bindings";

    // bind the opaque types
    pet::py::opaque(m);
    // register the exception types
    pet::py::exceptions(m);
    // version info
    pet::py::version(m);
}


// end of file
