# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the base class for magnetometer implementations
class Magnetometer(
    Instrument,
    family="pet.instruments.magnetometers.base",
    implements=pet.protocols.instruments.magnetometer,
):
    """
    The base class for magnetometer implementations
    """


# end of file
