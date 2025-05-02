# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Mode import Mode


# the state of the instrument when it is turned on; actual modes should derive from this class
class On(Mode, family="pet.instruments.modes.on"):
    """
    The mode that corresponds to the instrument being turned on and ready to operate.
    """

    # metamethods
    def __str__(self):
        """
        Human readable rendering of my state
        """
        # easy enough
        return "on"


# end of file
