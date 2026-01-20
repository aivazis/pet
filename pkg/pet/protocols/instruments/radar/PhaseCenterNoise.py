# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# noise characteristics for SAR phase centers
class PhaseCenterNoise(pet.protocol, family="pet.instruments.radar.phaseCenters.noise"):
    """
    The requirements for describing the noise characteristics of SAR instrument phase centers
    """

    # required state
    waveform = None
    coupling = None
    harmonics = None


# end of file
