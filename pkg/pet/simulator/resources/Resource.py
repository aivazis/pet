# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base resource
class Resource:
    """
    The base class for all mission resources
    """

    # interface
    def identify(self, consumer):
        """
        Invoke the resource handler of the {consumer}
        """
        # attempt to
        try:
            # ask the {consumer} for the base resource handler
            handler = consumer.resourceConsumption
        # if it doesn't understand
        except AttributeError:
            # get my class
            cls = type(self)
            # and my poorly formed visitor
            visitor = type(consumer)
            # it's not correctly formed since we only get here when all alternatives are exhausted
            raise NotImplementedError(
                f"class '{visitor.__module__}.{visitor.__name__}' "
                f"is not a '{cls.__module__}.{cls.__name__} visitor"
            ) from None
        # the base consumption curve is, by definition, resource agnostic, so it needs some
        # help to return dimensional quantities
        return lambda t: handler(t, resource=self)

    # implementation details
    units = pet.units.zero


# end of file
