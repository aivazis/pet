// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// get colors
import { wheel, theme } from '~/palette'
// get the base styles
import base from '~/views/styles'


// publish
export default {
    // the container
    extent: {
        // inherit
        ...base.panel,

        // fonts
        fontFamily: "inconsolata",
        fontSize: "60%",

        // make it stand out
        // margin: "1.0em",
        color: theme.page.name,
        backgroundColor: "hsl(0, 0%, 7%)",
    },

}


// end of file
