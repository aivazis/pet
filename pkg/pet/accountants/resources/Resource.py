# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base resource
class Resource(pet.component, implements=pet.protocols.accountants.resource):
    """
    The base class for all mission resources
    """

    # interface
    @pet.export
    def identify(self, consumer):
        """
        Retrieve the consumption curve for this resource from {consumer}
        """
        # attempt to
        try:
            # ask {consumer} for the base consumption curve
            curve = consumer.resourceConsumption
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
        return lambda t: curve(t, resource=self)

    # implementation details
    units = pet.units.zero


# end of file
