# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# superclass
from .Instrument import Instrument


# the NISAR instrument
class NISAR(
    Instrument, family="pet.instruments.nisar", implements=pet.protocols.instruments.sar
):
    """
    The NISAR instrument
    """

    # user configurable state
    # beam modes
    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.default = []
    modes.doc = "the list of beam modes supported by this instrument"

    # interface
    @pet.export
    def report(self, channel) -> None:
        """
        Render my configuration in the given journal {channel}
        """
        # chain up
        super().report(channel=channel)
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
