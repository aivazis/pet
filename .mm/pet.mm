# -*- makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# pet consists of a python package
pet.packages := pet.pkg
# libraries
pet.libraries := pet.lib
# python extensions
pet.extensions := pet.ext
# a ux bundle
pet.webpack := pet.ux
# and some tests
pet.tests := pet.lib.tests pet.ext.tests pet.pkg.tests

# docker images
# using ubuntu native package management
pet.native := \
  pet.dev.native.noble-gcc pet.dev.native.noble-clang \
  pet.dev.native.plucky-gcc pet.dev.native.plucky-clang \
# using micromamba built environments
pet.mamba := \
  pet.dev.mamba.noble-gcc pet.dev.mamba.noble-clang \
  pet.dev.mamba.plucky-gcc pet.dev.mamba.plucky-clang \

pet.docker-images := ${pet.native} #${pet.mamba}

# load the packages
include $(pet.packages)
# the libraries
include $(pet.libraries)
# the extensions
include $(pet.extensions)
# the ux
include $(pet.webpack)
# the test suites
include $(pet.tests)
# and the docker images
include ${pet.docker-images}


# end of file
