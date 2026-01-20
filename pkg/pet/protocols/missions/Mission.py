# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# parts
from .. import observatories


# the mission protocol
class Mission(pet.protocol, family="pet.missions"):
    """
    The mission requirements
    """

    # required state
    observatories = pet.properties.list(schema=observatories.observatory())
    observatories.doc = (
        "the constellation of observatories that carry the mission instruments"
    )


# end of file
