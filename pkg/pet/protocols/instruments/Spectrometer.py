# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the instrument protocol
class Spectrometer(Instrument, family="pet.instruments.spectrometers"):
    """
    Requirements for spectrometers
    """


# end of file
