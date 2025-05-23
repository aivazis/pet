# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# externals
import graphene

# query
from .Query import Query

# NYI: mutation
# from .Mutation import Mutation


# build the schema
schema = graphene.Schema(
    # supported operations
    query=Query,
    # mutation=Mutation,
)


# end of file
