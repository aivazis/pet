// -*- c++ -*-
// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved

// my declarations
#include "version.h"

// build and return the version tuple
auto
pet::version::version() -> version_t
{
    // easy enough
    return version_t { major, minor, micro, revision };
}

// end of file
