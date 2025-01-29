// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2025 all rights reserved


// externals
import React from 'react'
// locals
import styles from './styles'


const data = `
M 959.9456 296.1097
L 511.2964 82.54012
C 504.13664 79.153295 495.8116 79.153295 488.65185 82.54012
L 40.07608 296.1097
C 30.869194 300.4852 25.02172 309.77267 25.02172 319.98573
C 25.02172 330.17774 30.89019 339.48624 40.07608 343.84073
L 488.65185 557.3577 C 492.2422 559.06164 496.09505 559.9241 499.96887 559.9241
C 503.8532 559.9241 507.706 559.06164 511.2964 557.3577
L 959.9456 343.84073
C 969.1315 339.48624 975 330.17774 975 319.98573
C 975 309.77267 969.1315 300.4852 959.9456 296.1097
Z
M 499.96887 504.2309
L 112.8598 319.98573
L 499.96887 135.69848
L 887.1619 319.98573
Z
M 937.3116 476.14763
L 499.96887 684.2688
L 62.710106 476.14763
C 49.608406 469.81575 33.819177 475.4745 27.562275 488.67466
C 21.305373 501.8433 26.90089 517.5994 40.06558 523.8576
L 488.64136 737.3641
C 492.2317 739.068 496.08455 739.9305 499.95837 739.9305
C 503.8427 739.9305 507.6955 739.068 511.2859 737.3641
L 959.9456 523.86815
C 973.0893 517.5994 978.6849 501.8538 972.428 488.6852
C 966.2025 475.4745 950.4553 469.9104 937.3116 476.14763
Z
M 937.3116 656.1856
L 499.96887 864.3278
L 62.710106 656.1856
C 49.608406 649.9378 33.819177 655.5229 27.562275 668.7126
C 21.305373 681.8812 26.90089 697.65835 40.06558 703.9061
L 488.64136 917.4546
C 492.2317 919.1586 496.08455 920 499.95837 920
C 503.8427 920 507.6955 919.1586 511.2859 917.4546
L 959.9456 703.9061
C 973.0893 697.65835 978.6849 681.8812 972.428 668.7126
C 966.2025 655.53345 950.4553 649.9378 937.3116 656.1856
Z`


// render the shape
export const Data = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={data} style={ico} />
    )
}


// end of file
