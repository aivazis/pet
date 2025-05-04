# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# probes are craft
class Probe(Spacecraft, family="pet.observatories.probes"):
    """
    The probe requirements
    """


# end of file
