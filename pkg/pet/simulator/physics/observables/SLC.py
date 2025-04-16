# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# superclass
from .Observable import Observable


# a representation of the power and phase of radar echoes received from a target as a complex number
class SLC(Observable, family="pet.observables.slc"):
    """
    The amplitude and phase of a radar echo received from a target represented as a complex number
    """


# end of file
