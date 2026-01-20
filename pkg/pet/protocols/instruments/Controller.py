# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# my parts
from .Mode import Mode


# the instrument controller protocol
class Controller(pet.protocol, family="pet.instruments.controllers"):
    """
    The instrument controller requirements
    """

    # required state
    mode = Mode()
    mode.doc = "the current mode of the instrument"

    modes = pet.properties.list(schema=Mode())
    modes.doc = "the list of modes supported by this instrument"


# end of file
