# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument

# my parts
from .BeamMode import BeamMode


# the instrument protocol
class SAR(Instrument, family="pet.instruments.sar"):
    """
    Requirements for synthetic aperture radar instruments
    """

    # required state
    modes = pet.properties.list(schema=BeamMode())
    modes.doc = "the list of beam modes supported by this instrument"


# end of file
