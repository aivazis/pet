# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the data product writer protocol
class Writer(pet.flow.producer, family="pet.data.writers"):
    """
    The data product writer protocol
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data product"


# end of file
