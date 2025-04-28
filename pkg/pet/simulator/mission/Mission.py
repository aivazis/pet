# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base class for missions
class Mission(pet.component, implements=pet.protocols.missions.mission):
    """
    The base class for missions
    """

    # user configurable state
    craft = pet.properties.list(schema=pet.protocols.craft.craft())
    craft.doc = "the constellation of craft that carry the mission instruments"


# end of file
