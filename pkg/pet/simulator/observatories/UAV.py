# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Observatory import Observatory


# the base UAV implementation
class UAV(Observatory, implements=pet.protocols.observatories.uav):
    """
    Base class for all UAV implementations
    """


# end of file
