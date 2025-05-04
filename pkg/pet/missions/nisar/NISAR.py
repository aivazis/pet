# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet

# my parts
from .Orbiter import Orbiter


# the NISAR mission
class NISAR(pet.simulator.missions.mission, family="pet.missions.nisar"):
    """
    The NISAR mission
    """

    # user configurable state
    observatories = pet.properties.list(schema=pet.protocols.observatories.orbiter())
    observatories.default = []
    observatories.doc = (
        "the constellation of observatories that carry the mission instruments"
    )

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
        # go through my observatories
        for idx, observatory in enumerate(self.observatories):
            # mark
            channel.line(f"observatory {idx}:")
            # indent
            channel.indent()
            # ask the craft to report
            observatory.report(channel=channel)
            # and outdent
            channel.outdent()
        # outdent
        channel.outdent()
        # all done
        return

    # framework hooks
    def pyre_configured(self, **kwds):
        """
        Hook invoked after a NISAR mission instance is fully configured
        """
        # all done; chain up
        yield from super().pyre_configured(**kwds)
        # get my craft
        observatories = self.observatories
        # if the list is empty
        if not observatories:
            # the user has not expressed any opinions, so build the default craft
            primary = Orbiter(name=f"{self.pyre_name}.primary")
            # put in a list and attach it to the mission
            self.observatories = [primary]
        # all done
        return


# end of file
