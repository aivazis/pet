# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Mode import Mode


# mode transition model
class Transition(Mode, family="pet.instruments.modes.transition"):
    """
    The base class for modeling instrument mode transitions
    """

    # user configurable state
    this = pet.protocols.instruments.mode()
    this.doc = "the starting instrument mode"

    next = pet.protocols.instruments.mode()
    next.doc = "the mode to transition to"

    duration = pet.properties.dimensional()
    duration.doc = "the mode transition duration"


# end of file
