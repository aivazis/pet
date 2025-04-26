# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# get the basic modes
from . import modes


# the base class for instrument controllers
class Controller(
    pet.component,
    family="pet.instruments.controllers.base",
    implements=pet.protocols.instruments.controller,
):
    """
    The base class for all instruments
    """

    # required state
    mode = pet.protocols.instruments.mode()
    mode.default = modes.off()
    mode.doc = "the current instrument mode"

    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.default = [mode.default]
    modes.doc = "the list of modes supported by this instrument"

    # interface
    @pet.export
    def report(self, channel):
        """
        Render my state in the given journal {channel}
        """
        # sign on
        channel.line(f"{self}")
        # get my modes
        modes = self.modes
        # indent
        channel.indent()
        # report the current mode
        channel.line(f"mode: {self.mode}")

        # report the mode count
        channel.line(f"supported modes: {len(modes)}")
        # indent
        channel.indent()
        # go through the modes
        for mode in modes:
            # and report on each one
            channel.line(f"{mode}")
        # outdent
        channel.outdent()

        # outdent
        channel.outdent()
        # all done
        return


# end of file
