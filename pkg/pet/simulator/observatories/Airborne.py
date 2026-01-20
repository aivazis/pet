# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Observatory import Observatory


# the base airborne observatory
class Airborne(Observatory, implements=pet.protocols.observatories.airborne):
    """
    Base class for the implementation of airborne observatories
    """


# end of file
