# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# superclass
from .Beam import Beam


# requirements for fixed instrument beams
class FixedBeam(Beam, family="pet.instruments.radar.beams.fixed"):
    """
    Requirements for fixed instrument beams
    """

    # requirements
    pattern = None
    direction = None


# end of file
