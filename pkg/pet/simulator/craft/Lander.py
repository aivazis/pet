# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base lander
class Lander(
    Spacecraft, family="pet.craft.landers.base", implements=pet.protocols.craft.lander
):
    """
    A base lander
    """


# end of file
