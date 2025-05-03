# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Resource import Resource


# electrical power
class Power(Resource):
    """
    Electrical power as a consumable resource
    """

    # interface
    def identify(self, consumer):
        """
        Invoke the resource handler of the {consumer}
        """
        # attempt to
        try:
            # ask the {consumer} for the base resource handler
            handler = consumer.powerConsumption
        # if it doesn't understand
        except AttributeError:
            # chain up
            return super().identify(consumer=consumer)
        # if its has a consumption curve, return it
        return handler

    # implementation details
    units = pet.units.power.watt


# end of file
