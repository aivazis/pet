# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the data product protocol
class Product(pet.flow.specification, family="pet.data.products"):
    """
    The data product protocol
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the product source"


# end of file
