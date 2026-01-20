# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet
import journal


# declaration
class Debug(pet.shells.command, family="pet.cli.debug"):
    """
    Display debugging information about this application
    """

    # user configurable state
    root = pet.properties.str()
    root.default = None
    root.tip = "specify the portion of the namespace to display"

    full = pet.properties.bool()
    full.default = False
    full.tip = "control whether to do a full dive"

    @pet.export(tip="dump the application configuration namespace")
    def config(self, plexus, **kwds):
        """
        Generate a list of encountered configuration files
        """
        # make a channel
        channel = journal.info("pet.cli.config")
        # indent
        channel.indent()
        # get the configurator
        cfg = self.pyre_configurator
        # go through its list of sources
        for uri, priority in cfg.sources:
            # tell me
            channel.line(f"{uri}, priority '{priority.name}'")
        # outdent
        channel.outdent()
        # flush
        channel.log()

        # all done
        return 0

    @pet.export(tip="dump the application configuration namespace")
    def nfs(self, plexus, **kwds):
        """
        Dump the application configuration namespace
        """
        # get the prefix
        prefix = "pet" if self.root is None else self.root
        # and the name server
        nameserver = self.pyre_nameserver

        # make a channel
        channel = journal.info("pet.cli.nfs")
        # indent
        channel.indent()
        # get all nodes that match my {prefix}
        for info, node in nameserver.find(pattern=prefix):
            # attempt to
            try:
                # get the node value
                value = node.value
            # if anything goes wrong
            except nameserver.NodeError as error:
                # use the error message as the value
                value = f" ** ERROR: {error}"
            # inject
            channel.line(f"{info.name}: {value}")
        # outdent
        channel.outdent()
        # flush
        channel.log()

        # all done
        return 0

    @pet.export(tip="dump the application configuration namespace")
    def vfs(self, plexus, **kwds):
        """
        Dump the application virtual filesystem
        """
        # get the prefix as a path
        prefix = pet.primitives.path("/pet" if self.root is None else self.root)

        # starting at the root of the {vfs}
        folder = plexus.vfs
        # go through the {prefix} intermediate folder carefully
        for part in prefix.parts:
            # try to
            try:
                # look up the folder
                folder = folder[part]
            # if anything goes wrong
            except folder.NotFoundError:
                # make a channel
                channel = journal.error("merlin.debug.vfs")
                # complain
                channel.line(f"could not find '{part}' in '{folder.uri}'")
                channel.line(
                    f"while scanning for '{prefix}' in the virtual file system"
                )
                # flush
                channel.log()
                # and bail if errors aren't fatal
                return 1
            # if the folder exists, get its contents
            folder.discover(levels=1)

        # if the user wants to see everything
        if self.full:
            # dive
            folder.discover()

        # make a channel
        channel = journal.info("pet.cli.vfs")
        # sign in
        channel.line(f"vfs: prefix='{prefix}'")
        # indent
        channel.indent()
        # build the report
        channel.report(report=folder.dump())
        # outdent
        channel.outdent()
        # flush
        channel.log()

        # all done
        return 0


# end of file
