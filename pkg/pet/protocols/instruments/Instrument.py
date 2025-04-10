# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my part
from .Mode import Mode


# the instrument protocol
class Instrument(pet.protocol, family="pet.instruments"):
    """
    The instrument requirements
    """

    # required state
    mode = Mode()
    mode.doc = "the current mode of the instrument"

    modes = pet.properties.list(schema=Mode())
    modes.doc = "the list of beam modes supported by this instrument"


# end of file
