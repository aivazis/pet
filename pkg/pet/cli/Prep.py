# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# externals
import typing

# support
import pet
import journal


# declaration
class Prep(pet.shells.command, family="pet.cli.prep"):
    """
    Prepare a run
    """

    # user configurable state
    tools = pet.properties.list(schema=pet.protocols.tool())
    tools.doc = "the list of tools to invoke"

    mission = pet.protocols.mission()
    mission.doc = "the mission configuration"

    # the default entry point
    @pet.export(tip="prepare a run")
    def default(self, plexus, **kwds) -> typing.Literal[0]:
        """
        Prepare a run
        """
        # all done
        return 0

    @pet.export(tip="display the run configuration")
    def show(self, plexus, **kwds) -> typing.Literal[0]:
        """
        Generate a configuration report
        """
        # get the mission
        mission = self.mission
        # and the requested tools
        tools = self.tools

        # make a channel
        channel = journal.info("pet.cli.prep")
        # sing on
        channel.line(f"run configuration:")
        channel.indent()
        # mission
        if mission:
            # mark
            channel.line(f"mission: {mission}")
            # and show
            mission.show(channel=channel)
        # tools
        if tools:
            channel.line(f"tools:")
            channel.indent()
            for tool in tools:
                channel.line(f"{tool}")
            channel.outdent()
        channel.outdent()
        # flush
        channel.log()

        # all done
        return 0


# end of file
