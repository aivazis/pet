# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Observatory import Observatory


# ground installations
class Ground(Observatory, family="pet.observatories.ground"):
    """
    Fixed installations on the ground
    """


# end of file
