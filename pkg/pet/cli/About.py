# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet
import journal


# declaration
class About(pet.shells.command, family="pet.cli.about"):
    """
    Display information about this application
    """

    @pet.export(tip="print the copyright note")
    def copyright(self, plexus, **kwds):
        """
        Print the copyright note of the pet package
        """
        # show the copyright note
        plexus.info.log(pet.meta.copyright)
        # all done
        return

    @pet.export(tip="print out the acknowledgments")
    def credits(self, plexus, **kwds):
        """
        Print out the license and terms of use of the pet package
        """
        # show the package header
        plexus.info.log(pet.meta.header)
        # all done
        return

    @pet.export(tip="print out the license and terms of use")
    def license(self, plexus, **kwds):
        """
        Print out the license and terms of use of the pet package
        """
        # show the package license
        plexus.info.log(pet.meta.license)
        # all done
        return

    @pet.export(tip="print the version number")
    def version(self, plexus, **kwds):
        """
        Print the version of the pet package
        """
        # make a channel
        channel = journal.help("pet.about.version")

        # get the package version
        major, minor, micro, revision = pet.version()
        # show it
        channel.line(f"package: {major}.{minor}.{micro} rev {revision}")

        # get the bindings
        libpet = pet.libpet
        # if there are bindings
        if libpet:
            channel.line()
            channel.line(f"libpet:")
            # get the library version
            major, minor, micro, revision = libpet.libVersion
            # show it
            channel.line(f"  library: {major}.{minor}.{micro} rev {revision}")
            # get the version of the bindings
            major, minor, micro, revision = libpet.extVersion
            # show it
            channel.line(f"  bindings: {major}.{minor}.{micro} rev {revision}")

        # get the CUDA bindings
        libpet_cuda = pet.libpet_cuda
        # if there are bindings
        if libpet_cuda:
            channel.line()
            channel.line(f"libpet_cuda:")
            # get the library version
            major, minor, micro, revision = libpet_cuda.libVersion
            # show it
            channel.line(f"  library: {major}.{minor}.{micro} rev {revision}")
            # get the version of the bindings
            major, minor, micro, revision = libpet_cuda.extVersion
            # show it
            channel.line(f"  bindings: {major}.{minor}.{micro} rev {revision}")

        # flush
        channel.log()

        # all done
        return


# end of file
