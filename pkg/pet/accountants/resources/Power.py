# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Resource import Resource


# electrical power
class Power(Resource, family="pet.resources.power"):
    """
    Electrical power as a consumable resource
    """

    # interface
    @pet.export
    def identify(self, consumer):
        """
        Retrieve the power consumption curve from {consumer}
        """
        # attempt to
        try:
            # ask {consumer} for its power consumption curve
            curve = consumer.powerConsumption
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super().identify(consumer=consumer)
        # if its has a consumption curve, return it
        return curve

    # implementation details
    units = pet.units.power.watt


# end of file
