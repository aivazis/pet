# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Craft import Craft


# the platform that carries the mission instruments
class Spacecraft(Craft, family="pet.craft.spacecraft"):
    """
    Spacecraft requirements
    """

    # required state
    # the NAIF code used by spice to keep track of the spacecraft
    naif = pet.properties.int()
    naif.doc = "the NAIF id of the spacecraft"


# end of file
