# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the base class for altimeter implementations
class Altimeter(
    Instrument,
    family="pet.instruments.altimeters.base",
    implements=pet.protocols.instruments.altimeter,
):
    """
    The base class for altimeters
    """


# end of file
