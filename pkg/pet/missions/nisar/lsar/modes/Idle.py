# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the instrument is idle
class Idle(pet.simulator.instruments.modes.idle):
    """
    The instrument is idle
    """

    # configurable state
    power = pet.properties.dimensional()
    power.default = 1 * pet.units.power.watt

    # resource consumption
    def powerConsumption(self, t, **kwds):
        """
        Model power consumption while standby
        """
        # just chain up
        return self.power * t


# end of file
