# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# parts
from .. import missions


# the requirements for adjudicators
class Adjudicator(pet.protocol, family="pet.adjudicators"):
    """
    Requirements for adjudicators
    """

    # the mission
    mission = missions.mission()
    mission.doc = "the mission characteristics"


# end of file
