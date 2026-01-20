# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from ..Imager import Imager


# the base class for SAR instrument implementations
class SAR(Imager, implements=pet.protocols.instruments.radar.sar):
    """
    The base class for SAR instrument implementations
    """

    # phase centers
    receivers = pet.properties.tuple(
        schema=pet.protocols.instruments.radar.phaseCenter()
    )
    receivers.doc = "the collection of echo receivers"

    transmitters = pet.properties.tuple(
        schema=pet.protocols.instruments.radar.phaseCenter()
    )
    transmitters.doc = "the collection of pulse transmitters"


# end of file
