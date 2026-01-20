# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Observatory import Observatory


# instrument platforms that fly in an atmosphere
class Airborne(Observatory, family="pet.observatories.airborne"):
    """
    Requirements for airborne observatories
    """


# end of file
