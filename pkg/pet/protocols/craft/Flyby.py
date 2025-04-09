# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Craft import Craft


# flyby spacecraft are craft
class Flyby(Craft, family="pet.craft.flyby"):
    """
    The requirements for spacecraft that fly by a body
    """


# end of file
