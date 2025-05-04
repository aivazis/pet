# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from ..Imager import Imager

# parts
from .PhaseCenter import PhaseCenter


# the synthetic aperture radar protocol
class SAR(Imager, family="pet.instruments.sar"):
    """
    Requirements for synthetic aperture radar instruments
    """

    # phase centers
    receivers = pet.properties.tuple(schema=PhaseCenter())
    receivers.doc = "the collection of echo receivers"

    transmitters = pet.properties.tuple(schema=PhaseCenter())
    receivers.doc = "the collection of pulse transmitters"


# end of file
