#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


"""
Sanity check: verify that the {pet} package is accessible
"""

# support
import journal


# the driver
def test():
    # access the {pet} package
    import pet

    # make a channel
    channel = journal.debug("pet.pkg.tests.sanity")
    # show me
    channel.line(f"pet: {pet}")
    # flush
    channel.log()

    # all done
    return 0


# the main entry point
if __name__ == "__main__":
    # do...
    status = test()
    # and share
    raise SystemExit(status)


# end of file
