# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# superclass
from .Observable import Observable


# electromagnetic waves as an observable
class EM(Observable):
    """
    Electromagnetic waves as an observable quantity
    """

    polarization = None


# end of file
