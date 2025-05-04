# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base mission observatory
class Observatory(pet.component, implements=pet.protocols.observatories.observatory):
    """
    Base class for all observatory implementations
    """

    # required state
    instruments = pet.properties.list(schema=pet.protocols.instruments.instrument())
    instruments.doc = "the list of instruments on this observatory"


# end of file
