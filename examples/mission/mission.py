#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved

# support
import pet
import journal


# the app
class MissionApp(pet.application, family="pet.apps.mission"):
    """
    A simple application to showcase mission configuration
    """

    # user configurable state
    mission = pet.protocols.mission()
    mission.doc = "the mission"

    # application interface obligations
    @pet.export
    def main(self, *args, **kwds):
        """
        The main entry point
        """
        # get my mission
        mission = self.mission
        # if it's non-trivial
        if mission:
            # make a channel
            channel = journal.info("pet.app")
            # ask my mission to report its configuration
            mission.report(channel=channel)
            # and flush
            channel.log()
        # all done
        return 0


# bootstrap
if __name__ == "__main__":
    # instantiate the app
    app = MissionApp(name="pet.app")
    # launch it
    status = app.run()
    # and share its status with the shell
    raise SystemExit(status)


# end of file
