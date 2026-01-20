# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# superclass
from .Observatory import Observatory


# the base ground observatory
class Ground(Observatory, implements=pet.protocols.observatories.ground):
    """
    Base class for the implementation of ground observatories
    """


# end of file
