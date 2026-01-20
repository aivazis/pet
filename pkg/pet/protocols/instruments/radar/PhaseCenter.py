# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# my parts
from .Band import Band
from .Beam import Beam
from .PhaseCenterNoise import PhaseCenterNoise
from .Polarization import Polarization


# phase centers are parts of SAR instruments
class PhaseCenter(pet.protocol, family="pet.instruments.radar.phaseCenters"):
    """
    The requirements for SAR instrument phase centers
    """

    # required state
    location = pet.properties.tuple(schema=pet.properties.float())
    location.doc = "the location of the phase center in the instrument reference frame"

    beam = Beam()
    beam.doc = "the antenna beam characteristics"

    bands = pet.properties.tuple(schema=Band())
    bands.doc = "the collection of supported frequency bands"

    polarizations = pet.properties.tuple(schema=Polarization())
    polarizations.doc = "the collection of supported beam polarizations"

    noise = PhaseCenterNoise()
    noise.doc = "the noise characteristics of this phase center"


# end of file
