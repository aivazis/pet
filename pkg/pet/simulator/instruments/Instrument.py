# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my part
from .Mode import Mode


# the instrument protocol
class Instrument(
    pet.component,
    family="pet.instruments.base",
    implements=pet.protocols.instruments.instrument,
):
    """
    The instrument requirements
    """

    # required state
    modes = pet.properties.list(schema=Mode())
    modes.doc = "the list of beam modes supported by this instrument"

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
        # report the mode count
        channel.line(f"modes: {len(modes)}")
        # outdent
        channel.outdent()
        # all done
        return


# end of file
