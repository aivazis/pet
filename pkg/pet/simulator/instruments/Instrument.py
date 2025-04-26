# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# get the basic modes
from . import modes


# the base class for instruments
class Instrument(
    pet.component,
    family="pet.instruments.base",
    implements=pet.protocols.instruments.instrument,
):
    """
    The base class for all instruments
    """

    # required state
    controller = pet.protocols.instruments.controller()
    controller.doc = "the instrument controller"

    # interface
    @pet.export
    def report(self, channel):
        """
        Render my state in the given journal {channel}
        """
        # sign on
        channel.line(f"{self}")
        # indent
        channel.indent()
        # get my controller
        controller = self.controller
        # ask it to report
        controller.report(channel=channel)
        # outdent
        channel.outdent()
        # all done
        return


# end of file
