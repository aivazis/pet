# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Spacecraft import Spacecraft


# the base mission craft
class Probe(
    Spacecraft, family="pet.craft.probes.base", implements=pet.protocols.craft.probe
):
    """
    A base probe
    """


# end of file
