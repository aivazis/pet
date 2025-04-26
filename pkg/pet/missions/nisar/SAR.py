# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .Controller import Controller


# the NISAR instrument
class SAR(pet.simulator.instruments.sar, family="pet.missions.nisar.sar"):
    """
    The NISAR instrument
    """

    # user configurable state
    controller = pet.protocols.instruments.controller()
    controller.default = Controller
    controller.doc = "the NISAR instrument controller"


# end of file
