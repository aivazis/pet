# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Craft import Craft


# landers are craft
class Lander(Craft, family="pet.craft.landers"):
    """
    The requirements for spacecraft can land
    """


# end of file
