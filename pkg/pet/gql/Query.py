# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# externals
import graphene

# support
import pet


# types
from .PET import PET
from .Version import Version


# the query
class Query(graphene.ObjectType):
    """
    The top level query
    """

    # the known queries
    # the session manager
    pet = graphene.Field(PET)
    # server version info
    version = graphene.Field(Version, required=True)

    # the resolvers
    # the session manager
    @staticmethod
    def resolve_pet(root, info, **kwds):
        """
        Get the session layout
        """
        # grab the store
        store = info.context["store"]
        # and pass it on
        return store

    # version
    @staticmethod
    def resolve_version(root, info):
        """
        Build and return the server version
        """
        # supply the context for the {version} resolution
        return pet.meta


# end of file
