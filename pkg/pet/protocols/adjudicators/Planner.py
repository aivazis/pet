# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# parts
from .. import missions


# the requirements for mission planners
class Planner(pet.protocol, family="pet.adjudicators.planners"):
    """
    Requirements for mission planners
    """

    # the mission
    mission = missions.mission()
    mission.doc = "the mission characteristics"

    # the simulation window
    start = pet.properties.timestamp()
    start.doc = "the beginning of the simulation window"

    stop = pet.properties.timestamp()
    stop.doc = "the end of the simulation window"

    dt = pet.properties.dimensional()
    dt.doc = "the sampling "

    # interface obligations
    @pet.provides
    def plan(self):
        """
        Generate the mission plan
        """


# end of file
