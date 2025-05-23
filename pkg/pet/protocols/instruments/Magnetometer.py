# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the magnetometer protocol
class Magnetometer(Instrument, family="pet.instruments.magnetometers"):
    """
    Requirements for magnetometers
    """


# end of file
