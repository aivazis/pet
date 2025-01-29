// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved

// externals
// relay
import { graphql, useLazyLoadQuery } from 'react-relay/hooks'


// get the session manager
export const useFetchPET = () => {
    // ask for the session manager
    const { pet } = useLazyLoadQuery(
        // the query
        query,
        // the vars
        {},
        // the options
        { fetchPolicy: "network-only" }
    )
    // and return it
    return pet
}


const query = graphql`
    query useFetchPETQuery {
        pet {
            # the server side store id
            id
        }
    }
`


// end of file
