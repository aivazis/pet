# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# orbiters are craft
class Orbiter(Spacecraft, family="pet.craft.orbiters"):
    """
    The orbiter requirements
    """


# end of file
