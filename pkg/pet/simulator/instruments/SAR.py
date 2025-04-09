# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the base SAR instrument
class SAR(
    Instrument,
    family="pet.instruments.sar.base",
    implements=pet.protocols.instruments.sar,
):
    """
    The base SAR instrument
    """


# end of file
