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
class Standby(Mode, family="pet.instruments.modes.standby"):
    """
    The mode that corresponds to the instrument being on standby
    """

    # metamethods
    def __str__(self):
        """
        Human readable rendering of my state
        """
        # easy enough
        return "standby"


# end of file
