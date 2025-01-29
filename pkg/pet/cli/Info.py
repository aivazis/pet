# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet
import journal


# declaration
class Info(pet.shells.command, family="pet.cli.info"):
    """
    Display helpful information about various aspects of the application
    """

    @pet.export(tip="display host information")
    def host(self, plexus, **kwds):
        """
        Display information about the host
        """
        # get the host
        host = self.pyre_host

        # make a channel
        channel = journal.info("pet.info.host")
        # report
        channel.line(f"name: {host.hostname}")
        channel.line(f"nickname: {host.nickname}")
        channel.line(f"os: {host.distribution} {host.release} ({host.codename})")
        channel.line(f"arch: {host.cpus.architecture}")
        channel.line(f"cores: {host.cpus.cores}")
        # flush
        channel.log()

        # all done
        return

    @pet.export(tip="display platform information")
    def platform(self, plexus, **kwds):
        """
        Display information about the platform
        """
        # get the host
        host = self.pyre_host

        # unpack
        distribution = host.distribution
        release = host.release
        codename = host.codename
        arch = host.cpus.architecture
        tag = f"{host.tag}"

        # make a channel
        channel = journal.info("pet.info.platform")
        # report
        channel.line(f"os: {distribution} {release} ({codename})")
        channel.line(f"arch: {arch}")
        channel.line(f"tag: {tag}")
        # flush
        channel.log()

        # all done
        return

    @pet.export(tip="display user information")
    def user(self, plexus, **kwds):
        """
        Display information about the host
        """
        # get the host
        user = self.pyre_user

        # make a channel
        channel = journal.info("pet.info.user")
        # report
        channel.line(f"user: {user.username} ({user.uid})")
        channel.line(f"home: {user.home}")
        channel.line(f"name: {user.name}")
        channel.line(f"email: {user.email}")
        channel.line(f"affiliation: {user.affiliation}")
        # flush
        channel.log()

        # all done
        return


# end of file
