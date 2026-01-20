# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# observation requirements
class Objective(pet.protocol, family="pet.adjudicators.objectives"):
    """
    Requirements for mission objectives
    """

    # interface obligations
    @pet.provides
    def begin(self, mission, start, stop, **kwds):
        """
        Begin a mission simulation
        """

    @pet.provides
    def forecast(self, mission, t, stop, dt, **kwds):
        """
        Examine the proposed time window [t, t+dt] for activity relevant to this objective and
        suggest a more appropriate timestep
        """

    @pet.provides
    def advance(self, mission, t, dt, **kwds):
        """
        Examine the proposed time window [t, t+dt] for any activity relevant to this objective and
        return a list of the necessary actions
        """

    @pet.provides
    def end(self, mission, t, stop, **kwds):
        """
        Finish a mission simulation
        """


# end of file
