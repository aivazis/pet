# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the performance tool protocol
class Tool(pet.protocol, family="pet.tools"):
    """
    Requirements for performance tools
    """

    @pet.provides
    def prep(self, **kwds):
        """
        Prepare for a run
        """

    @pet.provides
    def run(self, **kwds):
        """
        Run the performance tool
        """

    @pet.provides
    def plot(self, **kwds):
        """
        Visualize the results
        """


# end of file
