# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .lsar.LSAR import LSAR


# the NISAR spacecraft
class Spacecraft(
    pet.component,
    family="pet.craft.orbiters.nisar",
    implements=pet.protocols.craft.orbiter,
):
    """
    The NISAR spacecraft
    """

    # configurable state
    # the NAIF code
    naif = pet.properties.int()
    naif.default = -198
    naif.doc = "the NAIF id of the NISAR spacecraft"

    # instruments carried by this spacecraft
    instruments = pet.properties.list(schema=pet.protocols.instruments.radar.sar())
    instruments.default = []
    instruments.doc = "the list of instruments carried by the NISAR spacecraft"

    # interface
    @pet.export
    def report(self, channel) -> None:
        """
        Render my configuration in the given journal {channel}
        """
        # sign on
        channel.line(f"{self}")
        # indent
        channel.indent()
        # show my NAIF code
        channel.line(f"NAIF id: {self.naif}")
        # go through my instruments
        for idx, instrument in enumerate(self.instruments):
            # mark
            channel.line(f"instrument {idx}:")
            # indent
            channel.indent()
            # visit
            instrument.report(channel=channel)
            # and outdent
            channel.outdent()
        # outdent
        channel.outdent()
        # all done
        return

    # framework hooks
    def pyre_configured(self, **kwds):
        """
        Hook invoked after a NISAR spacecraft instance is fully configured
        """
        # get my instruments
        instruments = self.instruments
        # if the list is empty
        if not instruments:
            # the user has not expressed any opinions, so build the default instrument
            instrument = LSAR(name=f"{self.pyre_name}.lsar")
            # put it in a list and attach it to this spacecraft
            self.instruments = [instrument]
        # all done; chain up
        return super().pyre_configured(**kwds)


# end of file
