#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


"""
Assemble a simple mission
"""


# support
import pet
import journal


# the driver
def test():
    # instantiate a mission
    mission = pet.missions.nisar(name="NISAR")
    # and a channel
    channel = journal.info("pet.missions")
    # ask the mission to report
    mission.report(channel=channel)
    # and flush
    channel.log()

    # all done
    return


# the main entry point
if __name__ == "__main__":
    # do...
    status = test()
    # and share
    raise SystemExit(status)


# end of file
