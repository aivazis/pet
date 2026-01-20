// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// pull the pages
import Intro from './intro'
import Design from './design'


// publish the content map
export const topics = [
    //
    {
        link: "intro", title: "Getting started", page: Intro,
        contents: [
            { link: "#intro.dependencies", title: "Dependencies" },
            { link: "#intro.cloning", title: "Cloning the repositories" },
            { link: "#intro.mm", title: "Setting up the build system" },
            { link: "#intro.building", title: "Building" },
            { link: "#intro.launching", title: "Launching" },
        ],
    },
    {
        link: "design", title: "Design", page: Design,
        contents: [
            { link: "#design.pyre", title: "Leveraging pyre" },
            { link: "#design.mission", title: "Fleshing out the mission abstractions" },
            { link: "#design.nisar", title: "Implementing the NISAR mission components" },
            { link: "#design.layout", title: "Package layout" },
            { link: "#design.reports", title: "Configuration reports" },
            { link: "#design.app", title: "Assembling a concrete mission" },
        ],
    },
]


// end of file
