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
        # ask the resource to identify itself and extract the resource consumption rate
        return resource.identify(consumer=self)

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

    # implementation details
    def resourceConsumption(self, t, resource, **kwds):
        """
        The handler for resources that this mode is not aware of
        """
        # by default, unknown resources are not consumed
        return 0 * resource.units


# end of file
