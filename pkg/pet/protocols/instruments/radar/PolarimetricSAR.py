# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .SAR import SAR


# the polarimetric SAR protocol
class PolarimetricSAR(SAR, family="pet.instruments.polarimetricSAR"):
    """
    Requirements for polarimetric SAR instruments
    """


# end of file
