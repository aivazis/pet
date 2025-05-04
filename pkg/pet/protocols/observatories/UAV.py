# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Observatory import Observatory


# the requirements for unmanned aerial vehicles
class UAV(Observatory, family="pet.observatories.uav"):
    """
    UAV requirements
    """


# end of file
