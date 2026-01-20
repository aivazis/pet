# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .SAR import SAR


# the base class for SAR instrument implementations
class PolarimetricSAR(SAR, implements=pet.protocols.instruments.radar.PolarimetricSAR):
    """
    The base class for polarimetric SAR instrument implementations
    """


# end of file
