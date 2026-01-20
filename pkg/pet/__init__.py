# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


"""
Contents:

  support for building the app:
    ext: home of the importable runtime assets that are the python bindings of low level code
    shells: support for application hosting strategies;
    cli: the command line interface
    ux: the client side of the graphical user interface (javascript, html, css, graphics, ...)
    gql: the server side of the app interface; uses graphql to expose the app state to clients

  protocols: the abstractions that define the capabilities of the package
  data: the supported data product formats, their readers and writers
  physics: the various science codes that model the physical processes observed by missions
  simulator: implementation of he mission simulation engine
  missions: planned or as-flown mission specifications, assembled from simulator parts
  performance: mission performance assessment
  accountants: the various mission "cost" assessors
  adjudicators: home of the mission optimizers
"""


# import and publish pyre symbols
from pyre import (
    # protocols, components, traits, and their infrastructure
    schemata,
    constraints,
    properties,
    protocol,
    component,
    foundry,
    descriptors,
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

# interfaces
from . import gql
from . import shells  # the supported application shells
from . import cli  # the command line interface
from . import ux  # support for the web client

# parts
from . import data
from . import physics
from . import simulator
from . import missions
from . import performance
from . import accountants
from . import adjudicators

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
