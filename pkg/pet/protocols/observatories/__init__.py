# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# the base class for all instrument hosts
from .Observatory import Observatory as observatory

# ground installations
from .Ground import Ground as ground

# aircraft
from .Airborne import Airborne as airborne
from .Aircraft import Aircraft as aircraft
from .UAV import UAV as uav

# spacecraft
from .Spacecraft import Spacecraft as spacecraft
from .Flyby import Flyby as flyby
from .Lander import Lander as lander
from .Orbiter import Orbiter as orbiter
from .Probe import Probe as probe


# end of file
