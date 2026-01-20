# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base orbiter
class Orbiter(Spacecraft, implements=pet.protocols.observatories.orbiter):
    """
    A base orbiter
    """


# end of file
