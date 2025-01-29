// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// externals
#include "external.h"
// namespace setup
#include "forward.h"

// the pet library
#include <pet/version.h>


// access to the version tags from the headers and the library
void
pet::py::version(py::module & m)
{
    // make a {version} submodule
    auto version = m.def_submodule(
        // its name
        "version",
        // its docstring
        "the static and dynamic version of the bindings");


    // add the static version
    version.def(
        // the name
        "static",
        // the implementation
        []() {
            // build a tuple from the static info in the headers
            auto extver = std::make_tuple(
                pet::version::major,
                pet::version::minor,
                pet::version::micro,
                pet::version::revision);
            // all done
            return extver;
        },
        // the docstring
        "the pet version visible at compile time");


    // add the dynamic version
    version.def(
        // the name
        "dynamic",
        // the implementation
        []() {
            // get the version as known to the pet shared library
            auto version = pet::version::version();
            // make a tuple
            auto libver = std::make_tuple(
                version.major,
                version.minor,
                version.micro,
                version.revision);
            // all done
            return libver;
        },
        // the docstring
        "the pet version visible through its shared library");


    // all done
    return;
}


// end of file
