# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Beam import Beam


# requirements for scanning instrument beams
class ScanningBeam(Beam, family="pet.instruments.radar.beams.scanning"):
    """
    Requirements for scanning instrument beams
    """

    # requirements
    pattern = None
    steering = None


# end of file
