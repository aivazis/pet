# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the NISAR instrument
class SAR(pet.simulator.instruments.sar, family="pet.missions.nisar.sar"):
    """
    The NISAR instrument
    """

    # user configurable state
    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.default = []
    modes.doc = "the list of beam modes supported by the NISAR instrument"


# end of file
