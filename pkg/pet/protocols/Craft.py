# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .Instrument import Instrument


# the platform that carries the mission instruments
class Craft(pet.protocol, family="pet.craft"):
    """
    The craft requirements
    """

    # required state
    instruments = pet.properties.list(schema=Instrument())
    instruments.doc = "the list of instruments on this craft"


# end of file
