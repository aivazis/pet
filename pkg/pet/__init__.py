# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# import and publish pyre symbols
from pyre import (
    # protocols, components, traits, and their infrastructure
    schemata,
    constraints,
    properties,
    protocol,
    component,
    foundry,
    # decorators
    export,
    provides,
    # the manager of the pyre runtime
    executive,
    # memory
    memory,
    # support for concurrency
    nexus,
    # support for workflows, products, and factories
    flow,
    # shells
    application,
    plexus,
    # miscellaneous
    primitives,
    timers,
    tracking,
    units,
    weaver,
)


# register the package with the framework
package = executive.registerPackage(name="pet", file=__file__)
# save the geography
home, prefix, defaults = package.layout()


# publish the local modules
# basic functionality
from . import meta
from . import exceptions

# the bindings
from .ext import libpet

# protocols
from . import protocols

# parts
from . import sol
from . import instruments
from . import missions

# schema
from . import gql

# user interfaces
from . import shells  # the supported application shells
from . import cli  # the command line interface
from . import ux  # support for the web client

# by convention
__version__ = meta.version


# administrivia
def copyright() -> None:
    """
    Return the copyright note
    """
    # pull and print the meta-data
    print(meta.header)
    # all done
    return


def license() -> None:
    """
    Print the license
    """
    # pull and print the meta-data
    print(meta.license)
    # all done
    return


def built() -> str:
    """
    Return the build timestamp
    """
    # pull and return the meta-data
    return meta.date


def credits() -> str:
    """
    Print the acknowledgments
    """
    return print(meta.acknowledgments)


def version() -> tuple[int, int, int, str]:
    """
    Return the version
    """
    # pull and return the meta-data
    return meta.version


# end of file
