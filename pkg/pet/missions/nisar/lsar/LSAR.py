# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .Controller import Controller


# the NISAR L-band instrument
class LSAR(pet.simulator.instruments.sar, family="pet.missions.nisar.lsar"):
    """
    The NISAR L-band instrument
    """

    # user configurable state
    controller = pet.protocols.instruments.controller()
    controller.default = Controller
    controller.doc = "the NISAR instrument controller"


# end of file
