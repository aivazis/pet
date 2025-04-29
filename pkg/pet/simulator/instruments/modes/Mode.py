# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# the base class for instrument modes
class Mode(pet.component, implements=pet.protocols.instruments.mode):
    """
    The base operational mode for all instrument types
    """

    # interface requirements
    @pet.export
    def consumes(self, resource):
        """
        Model the {resource} consumption by this mode as a function of time
        """
        # no, by default
        return lambda t: 0

    @pet.export
    def detects(self, observable):
        """
        Check whether this instrument mode can detect the given {observable}
        """
        # no, by default
        return False

    @pet.export
    def emits(self, observable):
        """
        Check whether this instrument mode can emit the given {observable}
        """
        # no, by default
        return False

    @pet.export
    def measures(self, observable):
        """
        Check whether this instrument mode can measure the given {observable}
        """
        # no, by default
        return False


# end of file
