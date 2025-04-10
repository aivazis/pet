# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Imager import Imager


# the base class for SAR instrument implementations
class SAR(
    Imager,
    family="pet.instruments.sar.base",
    implements=pet.protocols.instruments.sar,
):
    """
    The base class for SAR instrument implementations
    """


# end of file
