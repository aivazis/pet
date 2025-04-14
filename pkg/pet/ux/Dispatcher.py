# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# externals
import re
import signal

# support
import journal
import pet

# the query handler
from .GraphQL import GraphQL


# the main request dispatcher
class Dispatcher:
    """
    The handler of web requests
    """

    # interface
    def dispatch(self, plexus, server, request):
        """
        Analyze the {request} received by the {server} and invoke the appropriate {plexus} behavior
        """
        # get the request type
        command = request.command
        # get the request uri
        url = request.url

        # make a channel
        channel = journal.debug("pet.ux.dispatch.url")
        # and show me the {url}
        channel.log(f"{command}: {url}")

        # take a look
        match = self.regex.match(url)
        # if there is no match
        if not match:
            # we have a bug
            channel = journal.firewall("pet.ux.dispatch")
            # complain
            channel.line(f"could not find handler")
            channel.line(f"while resolving ${url}")
            # flush
            channel.log()
            # and return an error to the client
            return server.responses.NotFound(server=server)

        # find who matched
        token = match.lastgroup
        # look up the handler
        handler = getattr(self, token)
        # invoke
        return handler(plexus=plexus, server=server, request=request, match=match)

    # metamethods
    def __init__(self, plexus, docroot, pfs, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the location of my document root so i can serve static assets
        self.docroot = docroot.discover()
        # attach it to the app's private filesystem
        pfs["ux"] = docroot

        # make a spec for the app engine
        spec = "ux"
        # use the spec to build a name for my panel
        name = f"{plexus.pyre_name}.{spec}"
        # build the application store
        self.store = pet.ux.store(
            name=f"{plexus.pyre_name}.store",
            plexus=plexus,
            docroot=docroot,
            globalAliases=True,
        )
        # instantiate the {GraphQL} handler
        self.gql = GraphQL(plexus=plexus, dispatcher=self, store=self.store)

        # all done
        return

    # handlers
    def graphql(self, **kwds):
        """
        Handle a {graphql} request
        """
        # delegate to my {graphql} handler
        return self.gql.respond(store=self.store, **kwds)

    # basic handlers
    def stop(self, plexus, server, **kwds):
        """
        The client is asking me to die
        """
        # log it
        plexus.info.log("shutting down")
        # and exit
        return server.documents.Exit(server=server, code=128 + signal.SIGQUIT)

    def document(self, plexus, server, request, **kwds):
        """
        The client requested a document from the {plexus} pfs
        """
        # form the uri
        uri = "/ux" + request.url
        # open the document and serve it
        return server.documents.File(uri=uri, server=server, application=plexus)

    def css(self, plexus, server, request, **kwds):
        """
        The client requested a document from the {plexus} pfs
        """
        # form the uri
        uri = "/ux" + request.url
        # open the document and serve it
        return server.documents.CSS(uri=uri, server=server, application=plexus)

    def jscript(self, plexus, server, request, **kwds):
        """
        The client requested a document from the {plexus} pfs
        """
        # form the uri
        uri = "/ux" + request.url
        # open the document and serve it
        return server.documents.Javascript(uri=uri, server=server, application=plexus)

    def favicon(self, plexus, server, request, **kwds):
        """
        The client requested the app icon
        """
        # we don't have one
        return server.responses.NotFound(server=server)

    def root(self, plexus, server, request, **kwds):
        """
        The client requested the root document
        """
        # form the uri
        uri = "/ux/{0.pyre_namespace}.html".format(plexus)
        # open the document and serve it
        return server.documents.File(uri=uri, server=server, application=plexus)

    # private data
    # recognizer fragments
    uuid = r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}"
    pyreid = r"[^&?#:\s]+"
    zoom = r"-?\d+x-?\d+"
    origin = r"-?\d+x-?\d+"
    shape = r"\d+x\d+"
    # currently, only {csv} is supported
    profileFormat = r"(CSV)"

    # the app api
    regex = re.compile(
        "|".join(
            [
                # graphql requests
                r"/(?P<graphql>graphql)",
                # the kill command
                r"/(?P<stop>stop)",
                # document requests
                r"/(?P<css>.+\.css)",
                r"/(?P<jscript>.+\.js)",
                r"/(?P<document>(graphics/.+)|(fonts/.+)|(figures/.+)|(data/.+))",
                r"/(?P<favicon>favicon.ico)",
                # everything else gets the app page; see the {root} resolver above
                r"/(?P<root>.*)",
            ]
        )
    )


# end of file
