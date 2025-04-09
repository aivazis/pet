# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Craft import Craft


# the base flyby
class Flyby(
    Craft, family="pet.craft.flyby.base", implements=pet.protocols.craft.flyby
):
    """
    A base flyby craft
    """


# end of file
