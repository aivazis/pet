# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the radiometer protocol
class Radiometer(Instrument, family="pet.instruments.radiometers"):
    """
    Requirements for radiometers
    """


# end of file
