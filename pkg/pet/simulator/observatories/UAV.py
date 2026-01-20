# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Airborne import Airborne


# the base UAV implementation
class UAV(Airborne, implements=pet.protocols.observatories.uav):
    """
    Base class for all UAV implementations
    """


# end of file
