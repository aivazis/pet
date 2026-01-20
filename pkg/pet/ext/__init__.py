# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# attempt to
try:
    # pull the extension module
    from . import pet as libpet
# if this fails
except ImportError:
    # indicate the bindings are not accessible
    libpet = None


# end of file 
