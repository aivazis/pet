// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// external
import React from 'react'
import styled from 'styled-components'


// the markup
export const Pyre = () => (
    <PyreSpan>pyre</PyreSpan>
)

export const Protocol = styled.span`
    color: hsl(210deg, 70%, 50%);
    font-family: roboto;
    font-weight: lighter;
`

export const Component = styled.span`
    color: hsl(31deg, 95%, 50%);
    font-family: noto;
    font-weight: lighter;
`

// details
const PyreSpan = styled.span`
    font-family: rubik-light;
    color: hsl(63deg, 64%, 35%);
`


// end of file
