// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// get colors
import { theme } from '~/palette'

// the base style
import style from '~/shapes/styles'


// the shape color
const ink = theme.page.bright
const paint = theme.page.normal

// publish
export default {
    // the main shape
    icon: {
        // inherit
        ...style.icon,
        // stroke
        stroke: ink,
        strokeWidth: 1,
        // fill
        fill: "none",
    },

    // decorative touches
    decoration: {
        // inherit
        ...style.decoration,
        // stroke
        stroke: ink,
        strokeWidth: 0.5,
        // fill
        fill: "none",
    },
}


// end of file
