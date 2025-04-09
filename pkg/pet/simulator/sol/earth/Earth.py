# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the earth
class Earth(pet.component, family="pet.sol.earth", implements=pet.protocols.body):
    """
    A model for the Earth
    """

    # user configurable state
    name = pet.properties.str()
    name.default = "EARTH"
    name.doc = "the NAIF canonical name for earth"

    naif = pet.properties.int()
    naif.default = 399
    naif.doc = "the NAIF code for earth"

    frame = pet.properties.str()
    frame.default = "IAU_EARTH"
    frame.doc = "a frame of reference"


# end of file
