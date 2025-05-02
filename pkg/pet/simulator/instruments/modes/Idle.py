# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Mode import Mode


# the state of the instrument when it is on standby
class Idle(Mode, family="pet.instruments.modes.idle"):
    """
    The mode that corresponds to the instrument being powered on but idle
    """

    # metamethods
    def __str__(self):
        """
        Human readable rendering of my state
        """
        # easy enough
        return "idle"


# end of file
