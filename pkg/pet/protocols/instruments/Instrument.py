# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# my parts
from .Controller import Controller


# the instrument protocol
class Instrument(pet.protocol, family="pet.instruments"):
    """
    The instrument requirements
    """

    # required state
    controller = Controller()
    controller.doc = "the instrument controller"


# end of file
