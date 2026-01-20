# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# the earth
class Enceladus(
    pet.component, family="pet.sol.enceladus", implements=pet.protocols.body
):
    """
    A model for Enceladus
    """

    # user configurable state
    name = pet.properties.str()
    name.default = "ENCELADUS"
    name.doc = "the canonical NAIF name for enceladus"

    naif = pet.properties.str()
    naif.default = 602
    naif.doc = "the NAIF code for enceladus"


# end of file
