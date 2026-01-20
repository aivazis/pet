# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Mode import Mode


# the state of the instrument when it is turned off
class Off(Mode, family="pet.instruments.modes.off"):
    """
    The mode that corresponds to the instrument being turned off
    """

    # metamethods
    def __str__(self):
        """
        Human readable rendering of my state
        """
        # easy enough
        return "off"


# end of file
