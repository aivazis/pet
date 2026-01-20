# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the base writer
class Writer(
    pet.flow.factory,
    family="pet.writers.flat",
    implements=pet.protocols.data.writer,
):
    """
    The Flat writer
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data product"


# end of file
