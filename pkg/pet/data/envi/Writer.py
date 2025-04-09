# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the ENVI writer
class Writer(
    pet.flow.factory,
    family="pet.writers.envi",
    implements=pet.protocols.data.writer,
):
    """
    The ENVI writer
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data product"


# end of file
