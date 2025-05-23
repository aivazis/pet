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
    nyi: {
        // inherit
        ...base.panel,
    },

    placeholder: {
        position: "relative",
        top: "50%",
        left: "50%",
        width: "100%",
        height: "400px",
        textAlign: "center",
        transform: "translate(-50%, -50%)",
    },

    location: {
        color: theme.page.name,
    },

    icon: {
        // placement
        margin: "1.0em auto",
        width: "300px",
        height: "300px",

        // animation
        animationName: "fadeInOut",
        animationDuration: "3s",
        animationIterationCount: "infinite",
    },

    shape: {
        icon: {
            // stroke
            stroke: theme.page.name,
            strokeWidth: 3,
            // fill
            fill: "none",
        },
    },

    message: {
        fontFamily: "inconsolata",
        fontSize: "120%",
        textAlign: "center",
    },

}


// end of file
