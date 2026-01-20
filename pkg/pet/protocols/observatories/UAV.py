# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Airborne import Airborne


# the requirements for unmanned aerial vehicles
class UAV(Airborne, family="pet.observatories.uav"):
    """
    UAV requirements
    """


# end of file
