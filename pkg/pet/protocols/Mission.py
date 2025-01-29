# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .Craft import Craft


# the mission protocol
class Mission(pet.protocol, family="pet.missions"):
    """
    The mission requirements
    """

    # required state
    craft = pet.properties.list(schema=Craft())
    craft.doc = "the constellation of craft that carry the mission instruments"


# end of file
