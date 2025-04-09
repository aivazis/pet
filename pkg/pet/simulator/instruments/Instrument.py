# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base instrument
class Instrument(pet.component, implements=pet.protocols.instruments.instrument):
    """
    The base instrument
    """

    # required state
    modes = pet.properties.list(schema=pet.protocols.instruments.mode())
    modes.doc = "the list of beam modes supported by this instrument"

    # interface
    @pet.export
    def report(self, channel):
        """
        Render my state in the given journal {channel}
        """
        # sign on
        channel.line(f"{self}")
        # all done
        return


# end of file
