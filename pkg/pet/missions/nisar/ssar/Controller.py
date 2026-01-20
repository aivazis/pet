# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the NISAR instrument controller
class Controller(
    pet.simulator.instruments.controller, family="pet.missions.nisar.ssar.controller"
):
    """
    The NISAR instrument controller
    """

    # user configurable state
    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.default = [pet.simulator.instruments.controller.mode]
    modes.doc = "the list of beam modes supported by the NISAR SAR instruments"


# end of file
