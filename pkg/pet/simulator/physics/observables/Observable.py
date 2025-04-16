# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base class for observable quantities
class Observable(
    pet.component,
    family="pet.observables.base",
    implements=pet.protocols.data.observable,
):
    """
    The base class for observable quantities, i.e quantities that are measure by instruments
    and predicted by physics simulation codes
    """


# end of file
