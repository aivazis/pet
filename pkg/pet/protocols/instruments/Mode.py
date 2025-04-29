# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# requirements for instrument modes of operation
class Mode(pet.protocol, family="pet.instruments.modes"):
    """
    Requirements for instrument modes
    """

    # interface requirements
    @pet.provides
    def consumes(self, resource):
        """
        Model the {resource} consumption by this mode as a function of time
        """

    @pet.provides
    def detects(self, observable):
        """
        Check whether this instrument mode can detect the given {observable}
        """

    @pet.provides
    def measures(self, observable):
        """
        Check whether this instrument mode can measure the given {observable}
        """

    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Supply a default mode when one is not specified by the user
        """
        # instruments are off by default
        return pet.simulator.instruments.modes.off


# end of file
