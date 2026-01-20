# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# my parts
from .. import instruments


# the host of the mission instruments
class Observatory(pet.protocol, family="pet.observatories"):
    """
    The base class for the entities that host the mission hardware
    """

    # required state
    instruments = pet.properties.list(schema=instruments.instrument())
    instruments.doc = "the list of instruments on this craft"


# end of file
