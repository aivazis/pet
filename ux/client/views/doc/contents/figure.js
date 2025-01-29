// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// external
import React from 'react'
import styled from 'styled-components'


// the container
export const Figure = ({ src, width }) => {
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
`

// the image
const Image = styled.img`
    width: ${props => props?.width ?? "100%"};
`


// end of file
