# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet


# declaration
class Config(pet.shells.command, family="pet.cli.config"):
    """
    Display configuration information about this package
    """

    # version info
    @pet.export(tip="the version information")
    def version(self, **kwds):
        """
        Print the version of the pet package
        """
        # print the version number
        print(f"{pet.meta.version}")
        # all done
        return 0

    # configuration
    @pet.export(tip="the top level installation directory")
    def prefix(self, **kwds):
        """
        Print the top level installation directory
        """
        # print the installation location
        print(f"{pet.prefix}")
        # all done
        return 0

    @pet.export(tip="the directory with the executable scripts")
    def path(self, **kwds):
        """
        Print the location of the executable scripts
        """
        # print the path to the bin directory
        print(f"{pet.prefix}/bin")
        # all done
        return 0

    @pet.export(tip="the directory with the python packages")
    def pythonpath(self, **kwds):
        """
        Print the directory with the python packages
        """
        # print the path to the python package
        print(f"{pet.home.parent}")
        # all done
        return 0

    @pet.export(tip="the location of the {pet} headers")
    def incpath(self, **kwds):
        """
        Print the locations of the {pet} headers
        """
        # print the path to the headers
        print(f"{pet.prefix}/include")
        # all done
        return 0

    @pet.export(tip="the location of the {pet} libraries")
    def libpath(self, **kwds):
        """
        Print the locations of the {pet} libraries
        """
        # print the path to the libraries
        print(f"{pet.prefix}/lib")
        # all done
        return 0


# end of file
