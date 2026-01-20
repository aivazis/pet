// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// externals
import React from 'react'

// local
// context
import { Context } from './context'


// access to the registered views
export const usePET = () => {
    // grab the list of {views} from context
    const { pet } = React.useContext(Context)
    // and return it
    return pet
}


// end of file
