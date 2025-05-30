# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# access the pyre framework
import pyre
# my protocol
from .Action import Action as action


# class declaration
class Command(pyre.panel(), implements=action):
    """
    Base class for {pet} commands
    """


# end of file
