# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# flat binary products
class Flat(
    pet.flow.product,
    family="pet.products.flat",
    implements=pet.protocols.data.product,
):
    """
    Flat binary files in native format
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data header"

    cell = pet.properties.cell()
    cell.doc = "the specification of the product data type"

    shape = pet.properties.tuple(schema=pet.properties.int())
    shape.default = None
    shape.doc = "the shape of the product payload"

    # metamethods
    def __init__(self, data=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # realize my payload
        self.data = data
        # all done
        return


# end of file
