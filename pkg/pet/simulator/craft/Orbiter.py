# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base mission craft
class Orbiter(
    Spacecraft, family="pet.craft.orbiters.base", implements=pet.protocols.craft.orbiter
):
    """
    A base orbiter
    """


# end of file
