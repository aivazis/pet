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

    # framework hooks
    @classmethod
    def pyre_default(cls, **kwds):
        """
        Supply a default mode when one is not specified by the user
        """
        # instruments are off by default
        return pet.instruments.modes.off


# end of file
