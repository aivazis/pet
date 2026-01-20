# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Airborne import Airborne


# the base class for aircraft that host instruments
class Aircraft(Airborne, implements=pet.protocols.observatories.aircraft):
    """
    Base class for aircraft that carry instruments
    """


# end of file
