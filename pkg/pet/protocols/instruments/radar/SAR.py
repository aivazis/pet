# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from ..Imager import Imager


# the synthetic aperture radar protocol
class SAR(Imager, family="pet.instruments.radar.sar"):
    """
    Requirements for synthetic aperture radar instruments
    """


# end of file
