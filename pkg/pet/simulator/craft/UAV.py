# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Craft import Craft


# the base UAV implementation
class UAV(Craft, family="pet.craft.uav.base", implements=pet.protocols.craft.uav):
    """
    Base class for all UAV implementations
    """


# end of file
