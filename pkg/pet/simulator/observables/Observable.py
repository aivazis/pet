# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# the base class for observable quantities
class Observable:
    """
    The base class for observable quantities

    This is meant to represent physical quantities that detectors can detect. A slight kink in the
    naming is the fact that instruments can be sources of their observables. e.g. radars illuminate
    their targets and then detect the reflected radiation. so perhaps there is a better word for
    this.
    """


# end of file
