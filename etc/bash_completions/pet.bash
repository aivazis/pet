# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved

# bash completion script for pet
function _pet() {
    # get the partial command line
    local line=${COMP_LINE}
    local word=${COMP_WORDS[COMP_CWORD]}
    # ask pet to provide guesses
    COMPREPLY=($(pet complete --word="${word}" --line="${line}"))
}

# register the hook
complete -F _pet pet

# end of file
