# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# observation requirements
class Plan(
    pet.component, family="pet.ops.plans.base", implements=pet.protocols.ops.plan
):
    """
    The base mission plan
    """


# end of file
