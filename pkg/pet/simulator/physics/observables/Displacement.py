# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Observable import Observable


# encapsulation of the difference in position of a target between two measurements
class Displacement(Observable, family="pet.observables.slc"):
    """
    The difference in the position of a target between two measurements
    """


# end of file
