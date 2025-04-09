# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Craft import Craft


# the base mission craft
class Orbiter(
    Craft, family="pet.craft.orbiters.base", implements=pet.protocols.craft.orbiter
):
    """
    A base orbiter
    """


# end of file
