# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the data product writer protocol
class Reader(pet.flow.producer, family="pet.data.readers"):
    """
    The data product reader protocol
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data product"


# end of file
