# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# my parts
from .PulsePlan import PulsePlan
from .SignalCode import SignalCode


# requirements for the frequency bands supported by a phase center
class Band(pet.protocol, family="pet.instruments.radar.bands"):
    """
    Requirements for the frequency bands supported by a phase center
    """

    # requirements
    code = SignalCode()
    code.doc = "the code per pulse that provides spectral content"

    pulses = PulsePlan()
    pulses.doc = "the pulse plan for the band waveform"


# end of file
