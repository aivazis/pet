# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the base class for photometer implementations
class Photometer(
    Instrument,
    family="pet.instruments.photometers.base",
    implements=pet.protocols.instruments.radiometer,
):
    """
    The base class for photometer implementations
    """


# end of file
