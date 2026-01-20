# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base lander
class Lander(Spacecraft, implements=pet.protocols.observatories.lander):
    """
    A base lander
    """


# end of file
