# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base flyby
class Flyby(Spacecraft, implements=pet.protocols.observatories.flyby):
    """
    A base flyby spacecraft
    """


# end of file
