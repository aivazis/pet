# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Airborne import Airborne


# the requirements for aircraft that host instruments
class Aircraft(Airborne, family="pet.observatories.aircraft"):
    """
    Requirements for aircraft
    """


# end of file
