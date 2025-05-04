# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Observatory import Observatory


# the base mission spacecraft
class Spacecraft(Observatory, implements=pet.protocols.observatories.spacecraft):
    """
    Base class for all spacecraft implementations
    """

    # required state
    # the NAIF code used by spice to keep track of the spacecraft
    naif = pet.properties.int()
    naif.default = None  # missions must obtain and assign codes to their craft
    naif.doc = "the NAIF id of the spacecraft"


# end of file
