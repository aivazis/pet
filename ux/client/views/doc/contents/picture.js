// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// external
import React from 'react'
import styled from 'styled-components'


// the container
export const Picture = ({ src, width }) => {
    // render
    return (
        <Box>
            <Image src={src} width={width} />
        </Box>
    )
}


// the box
const Box = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1.0rem;
    padding: 1.0em;
    background-color: hsl(0deg, 0%, 7%);
    border: 1px solid hsl(0deg, 0%, 15%);
    border-radius: 0.5em;
`

// the image
const Image = styled.img`
    width: ${props => props?.width ?? "100%"};
`


// end of file
