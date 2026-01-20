# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# instrument modes
from . import modes

# instrument control
from .Controller import Controller as controller

# the base instrument
from .Instrument import Instrument as instrument

# other instrument types
from .Altimeter import Altimeter as altimeter
from .Imager import Imager as imager
from .Magnetometer import Magnetometer as magnetometer
from .Radiometer import Radiometer as radiometer

# radar
from . import radar


# end of file
