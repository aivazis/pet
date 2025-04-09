# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2025 all rights reserved


# support
import pet
import journal

# the data product
from .ENVI import ENVI


# the ENVI reader
class Reader(
    pet.flow.factory,
    family="pet.readers.envi",
    implements=pet.protocols.data.reader,
):
    """
    The ENVI reader
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data product"

    # interface
    def open(self):
        """
        Extract the ENVI header info
        """
        # open the file
        with open(str(self.uri), mode="r") as hdr:
            # get the first line
            marker = next(hdr).strip()
            # if it's not the magic string
            if marker != "ENVI":
                # make a channel
                channel = journal.warning("pet.data.envi.reader")
                # complain
                channel.line(f"while parsing '{self.uri}'")
                channel.indent()
                channel.line("missing ENVI marker in the first line of the file")
                channel.outdent()
                # flush
                channel.log()
                # bail
                return

            # extract the fields
            fields = self.parse(hdr=hdr)
            # build the product
            envi = ENVI(name=f"{self.pyre_name}.data", uri=self.uri, **fields)
            # and return it
            return envi

        # all done
        return

    # implementation details
    def parse(self, hdr):
        """
        Extract the ENVI header fields
        """
        # start a pile
        fields = {}

        # go through the file contents
        for line in hdr:
            # strip
            line = line.strip()
            # if it's a comment
            if line.startswith(";"):
                # ignore it
                continue

            # parse the assignment
            field, value = line.split("=")
            # strip
            field = field.strip()
            value = value.strip()

            # if the value has an opening brace
            if "{" in value:
                # if it also has the matching closing brace
                if "}" in value:
                    # extract just the part between the two delimiters
                    value = value[value.index("{") + 1 : value.index("}")].strip()
                # if not
                else:
                    # make a pile
                    text = [value[value.index("{") + 1 :].strip()]
                    # collect the rest
                    for more in hdr:
                        # strip
                        more = more.strip()
                        # if this line contains the terminator
                        if "}" in more:
                            # collect the part up to the closing brace
                            text.append(more[: more.index("}")])
                            # reconstruct the value
                            value = " ".join(filter(None, text))
                            # and move on
                            break
                        # if not
                        else:
                            # accumulate the text
                            text.append(more)
            # save
            fields[field] = value

        # all done
        return fields


# end of file
