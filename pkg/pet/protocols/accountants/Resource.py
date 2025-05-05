# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# requirements for the quantities accountants care about
class Resource(pet.protocol, family="pet.accountants.resources"):
    """
    Requirements for the various quantities that accountants keep track of
    """

    # required interface
    @pet.provides
    def identify(self, consumer, **kwds):
        """
        Retrieve the consumption curve for this resource from {consumer}
        """


# end of file
