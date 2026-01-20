# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet

# the data product
from .Flat import Flat


# reader for flat binary data products
class Reader(
    pet.flow.factory,
    family="pet.readers.flat",
    implements=pet.protocols.data.reader,
):
    """
    The base reader for flat binary data products in native representations
    """

    # required state
    uri = pet.properties.uri()
    uri.default = None
    uri.doc = "the location of the data product"

    hdr = pet.properties.uri()
    hdr.default = None
    hdr.doc = "the location of the ENVI header"

    # interface
    def open(self):
        """
        Build the data product
        """
        # make a reader for the header file
        headerReader = pet.data.envi.reader(uri=self.hdr)
        # load the header
        hdr = headerReader.open()
        # unpack the metadata
        shape = hdr.samples, hdr.lines
        cell = hdr.cell(const=True)
        # build the data buffer
        data = pet.memory.mapgrid(uri=self.uri, type=cell, shape=shape)
        # build the product
        flat = Flat(
            # the name
            name=f"{self.pyre_name}.data",
            # product location
            uri=self.uri,
            # metadata
            shape=shape,
            cell=cell,
            data=data,
        )
        # and return it
        return flat

    # framework hooks
    def pyre_configured(self, **kwds):
        """
        Hook invoked after the reader is configured
        """
        # get the header uri
        headerURI = self.hdr
        # if the user hasn't provided a URI for the header
        if headerURI is None:
            # get the product uri
            productURI = self.uri
            # get its address
            productPath = pet.primitives.path(productURI.address)
            # adjust the suffix to form the path to the header
            hdrPath = productPath.withSuffix(suffix=".hdr")
            # for the uri to the header
            headerURI = productURI.clone(address=hdrPath)
            # and store
            self.hdr = headerURI
        # chain up
        yield from super().pyre_configured(**kwds)
        # all done
        return


# end of file
