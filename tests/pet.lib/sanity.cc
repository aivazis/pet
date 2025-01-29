// -*- C++ -*-
// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// get the journal
#include <pyre/journal.h>
// get the {pet} version
#include <pet/version.h>


// the driver
int main(int argc, char *argv[])
{
    // configure journal
    pyre::journal::application("sanity");
    pyre::journal::init(argc, argv);

    // make a channel
    auto channel = pyre::journal::debug_t("pet.sanity");

    // get the {pet} version
    auto version = pet::version::version();

    // say something
    channel
        << "version: " << pyre::journal::newline
        // the static version, straight from the headers
        << "   static: "
        << pet::version::major << "."
        << pet::version::minor << "."
        << pet::version::micro << "."
        << pet::version::revision << pyre::journal::newline
        // the dynamic version, from the library
        << "  dynamic: "
        << version.major << "."
        << version.minor << "."
        << version.micro << "."
        << version.revision << "."
        << pyre::journal::endl(__HERE__);

    // all done
    return 0;
}


// end of file
