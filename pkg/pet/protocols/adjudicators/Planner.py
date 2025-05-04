# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Adjudicator import Adjudicator


# the requirements for mission planners
class Planner(Adjudicator, family="pet.adjudicators.planners"):
    """
    Requirements for mission planners
    """

    # the simulation window
    start = pet.properties.timestamp()
    start.doc = "the beginning of the simulation window"

    stop = pet.properties.timestamp()
    stop.doc = "the end of the simulation window"

    dt = pet.properties.dimensional()
    dt.doc = "the sampling interval"

    # interface obligations
    @pet.provides
    def plan(self):
        """
        Generate the mission plan
        """


# end of file
