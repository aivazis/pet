# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# the instrument modes
from .modes import off, standby, idle


# the NISAR instrument controller
class Controller(
    pet.simulator.instruments.controller, family="pet.missions.nisar.lsar.controller"
):
    """
    The NISAR L-band instrument controller
    """

    # user configurable state
    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.default = None
    modes.doc = "the list of beam modes supported by the NISAR SAR instruments"

    # framework hooks
    def pyre_configured(self):
        # chain up
        yield from super().pyre_configured()

        # get my modes
        modes = self.modes
        # if the user hasn't set any
        if modes is None:
            # make a pile
            modes = [
                # off
                off(name=f"{self.pyre_name}.off"),
                # standby
                standby(name=f"{self.pyre_name}.standby"),
                # idle
                idle(name=f"{self.pyre_name}.idle"),
            ]
            # and attach it
            self.modes = modes

        # all done
        return


# end of file
