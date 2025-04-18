// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// publish
// the main page
export { Main, useTopic, useActivityPanel } from './main'
// embedded documentation
export { Guide, TOC } from './doc'

// the status bar
export { Status } from './status'

// blank panel
export { Blank } from './blank'
// not yet implemented
export { NYI } from './nyi'
// while {suspense} is waiting
export { Loading } from './loading'
// the page rendered when the user kills the server and support for the {kill} button
export { Stop, Dead } from './stop'


// end of file
