# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the altimeter protocol
class Altimeter(Instrument, family="pet.instruments.altimeters"):
    """
    Requirements for altimeters
    """


# end of file
