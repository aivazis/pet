# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2026 all rights reserved


# support
import pet


# metadata in ENVI form
class ENVI(
    pet.flow.product,
    family="pet.products.envi",
    implements=pet.protocols.data.product,
):
    """
    Product metadata in ENVI form

    Source: https://www.nv5geospatialsoftware.com/docs/ENVIHeaderFiles.html on 20250302
    """

    # required state
    uri = pet.properties.uri()
    uri.doc = "the location of the data header"

    # the fields
    acquisitionTime = pet.properties.timestamp()
    acquisitionTime.aliases.update(("acquisition time",))
    acquisitionTime.doc = "data acquisition time that conforms to the iso-8601 standard"

    bandNames = pet.properties.strings()
    bandNames.aliases = {"band names"}
    bandNames.doc = "the names of image bands"

    bands = pet.properties.int()
    bands.doc = "the number of bands per image file"

    bbl = pet.properties.list(schema=pet.properties.int())
    bbl.doc = "the bad band multiplier values for each band in the image"

    byteOrder = pet.properties.int()
    byteOrder.aliases = {"byte order"}
    byteOrder.doc = "the order of bytes in numeric data"

    classLookup = pet.properties.list(schema=pet.properties.int())
    classLookup.aliases = {"class lookup"}
    classLookup.doc = "rgb class colors for classification files"

    classNames = pet.properties.strings()
    classNames.aliases = {"class names"}
    classNames.doc = "the class names for classification files"

    classes = pet.properties.int()
    classes.doc = "the number of pixel classes for classification files"

    cloudCover = pet.properties.float()
    cloudCover.aliases = {"cloud cover"}
    cloudCover.doc = "percentage of cloud cover within the raster"

    colorTable = pet.properties.tuple(schema=pet.properties.int())
    colorTable.aliases = {"color table"}
    colorTable.doc = "default color table to use; a 3 x 256 array of bytes"

    complexFunction = pet.properties.str()
    complexFunction.default = "Power"
    complexFunction.aliases = {"complex function"}
    complexFunction.validators = pet.constraints.isMember(
        "Real", "Imaginary", "Power", "Magnitude", "Phase"
    )
    complexFunction.doc = "specifies the values to extract from a complex image"

    coordinateSystem = pet.properties.str()
    coordinateSystem.aliases = {"coordinate system string"}
    coordinateSystem.doc = "the ENVI coordinate system identifier"

    dataGain = pet.properties.tuple(schema=pet.properties.float())
    dataGain.aliases = {"data gain values"}
    dataGain.doc = "gain values for each band"

    dataIgnore = pet.properties.tuple(schema=pet.properties.float())
    dataIgnore.aliases = {"data ignore values"}
    dataIgnore.doc = "pixel values that should be ignored in image processing"

    dataOffset = pet.properties.tuple(schema=pet.properties.float())
    dataOffset.aliases = {"data offset values"}
    dataOffset.doc = "offset values for each band"

    dataReflectanceGain = pet.properties.tuple(schema=pet.properties.float())
    dataReflectanceGain.aliases = {"data reflectance gain values"}
    dataReflectanceGain.doc = "an array of data reflectance gain values"

    dataReflectanceOffset = pet.properties.tuple(schema=pet.properties.float())
    dataReflectanceOffset.aliases = {"data reflectance offset values"}
    dataReflectanceOffset.doc = "an array of data reflectance offset values"

    dataGain = pet.properties.tuple(schema=pet.properties.float())
    dataType = pet.properties.int()
    dataType.aliases = {"data type"}
    dataType.doc = "the type of data representation"

    defaultBands = pet.properties.tuple(schema=pet.properties.int())
    defaultBands.aliases = {"default bands"}
    defaultBands.doc = "the band numbers to automatically load"

    defaultStretch = pet.properties.str()
    defaultStretch.aliases = {"default stretch"}
    defaultStretch.doc = "the type of stretch to use"

    demBand = pet.properties.int()
    demBand.aliases = {"dem band"}
    demBand.doc = "the 1-based index of the DEM band associated with the image"

    dem = pet.properties.path()
    dem.aliases = {"dem file"}
    dem.doc = "the path to a DEM associated with the image"

    description = pet.properties.str()
    description.doc = "string describing the image or the processing performed "

    fileType = pet.properties.str()
    fileType.aliases = {"file type"}
    fileType.doc = "the ENVI file type"

    geoPoints = pet.properties.tuple(schema=pet.properties.float())
    geoPoints.aliases = {"geo points"}
    geoPoints.doc = "geographic corners for non-georeferenced files"

    headerOffset = pet.properties.int()
    headerOffset.default = 0
    headerOffset.aliases = {"header offset"}
    headerOffset.doc = "the number of bytes of embedded header information in the file"

    interleave = pet.properties.str()
    interleave.default = None
    interleave.validators = pet.constraints.isMember("bsq", "bil", "bip")
    interleave.doc = "the data interleave; one of bsq, bil, bip"

    lines = pet.properties.int()
    lines.doc = "the number of lines per image for each band"

    mapInfo = pet.properties.str()
    mapInfo.aliases = {"map info"}
    mapInfo.doc = "geographic information"

    pixelSize = pet.properties.tuple(schema=pet.properties.float())
    pixelSize.aliases = {"pixel size"}
    pixelSize.doc = "indicates x and y pixel size in meters"

    projectionInfo = pet.properties.str()
    projectionInfo.aliases = {"projection info"}
    projectionInfo.doc = "custom projection information"

    readProcedures = pet.properties.strings()
    readProcedures.aliases = {"read procedures"}
    readProcedures.doc = "the names of spatial and spectral read routines"

    reflectanceScaleFactor = pet.properties.float()
    reflectanceScaleFactor.aliases = {"reflectance scale factor"}
    reflectanceScaleFactor.doc = (
        "the factor needed to scale reflectance to the [0,1] region"
    )

    rpcInfo = pet.properties.strings()
    rpcInfo.aliases = {"rpc info"}
    rpcInfo.doc = "rational polynomial coefficient geolocation information"

    samples = pet.properties.int()
    samples.doc = "the number of samples per image line for each band"

    securityTag = pet.properties.str()
    securityTag.aliases = {"security tag"}
    securityTag.doc = (
        "information inherited from formats that contain classification levels"
    )

    sensorType = pet.properties.str()
    sensorType.aliases = {"sensor type"}
    sensorType.doc = "instrument type"

    solarIrradiance = pet.properties.tuple(schema=pet.properties.float())
    solarIrradiance.aliases = {"solar irradiance"}
    solarIrradiance.doc = (
        "top of the atmosphere solar irradiance per band; in W/(m^2 * μm)"
    )

    spectraNames = pet.properties.strings()
    spectraNames.aliases = {"spectra names"}
    spectraNames.doc = "a comma separated list of spectra names"

    sunAzimuth = pet.properties.float()
    sunAzimuth.aliases = {"sun azimuth"}
    sunAzimuth.doc = "angle of the sun, in degrees, clockwise from due north"

    sunElevation = pet.properties.float()
    sunElevation.aliases = {"sun elevation"}
    sunElevation.doc = "angle of the sun above the horizon, in degrees"

    timestamp = pet.properties.strings()
    timestamp.doc = "the timestamp names of temporal cube bands"

    wavelength = pet.properties.float()
    wavelength.doc = "the center wavelength values of each band"

    wavelengthUnits = pet.properties.str()
    wavelengthUnits.aliases = {"wavelength units"}
    wavelengthUnits.doc = "the wavelength units"

    xStart = pet.properties.tuple(schema=pet.properties.float())
    xStart.aliases = {"x start"}
    xStart.doc = "the image coordinates for the upper left pixel"

    yStart = pet.properties.tuple(schema=pet.properties.float())
    yStart.aliases = {"y start"}
    yStart.doc = "the image coordinates for the upper left pixel"

    zPlotAverage = pet.properties.int()
    zPlotAverage.aliases = {"z plot average"}
    zPlotAverage.doc = (
        "the number of pixels in the x and y direction to average for Z plots"
    )

    zPlotRange = pet.properties.tuple(schema=pet.properties.float())
    zPlotRange.aliases = {"z plot range"}
    zPlotRange.doc = "the default minimum and maximum values for Z plots"

    zPlotTitles = pet.properties.strings()
    zPlotTitles.aliases = {"z plot titles"}
    zPlotTitles.doc = "the x and y axis titles for Z plots"

    # normalizer registration
    @pet.descriptors.normalizer(traits=[interleave])
    def lower(value: str, **kwds) -> str:
        # convert {value} to lower case
        return value.lower()

    # interface
    def cell(self, const=True):
        """
        Convert my data type to the corresponding {pyre} memory {cell}
        """
        # pick the cell container
        table = self._constCells if const else self._mutableCells
        # look up the type and return it
        return table[self.dataType]()

    # implementation details
    _constCells = [
        None,
        pet.memory.cells.uint8Const,
        pet.memory.cells.int16Const,
        pet.memory.cells.int32Const,
        pet.memory.cells.floatConst,
        pet.memory.cells.doubleConst,
        pet.memory.cells.complexFloatConst,
        None,
        None,
        pet.memory.cells.complexDoubleConst,
        None,
        None,
        pet.memory.cells.uint16Const,
        pet.memory.cells.uint32Const,
        pet.memory.cells.int64Const,
        pet.memory.cells.uint64Const,
    ]

    _mutableCells = [
        None,
        pet.memory.cells.uint8,
        pet.memory.cells.int16,
        pet.memory.cells.int32,
        pet.memory.cells.float,
        pet.memory.cells.double,
        pet.memory.cells.complexFloat,
        None,
        None,
        pet.memory.cells.complexDouble,
        None,
        None,
        pet.memory.cells.uint16,
        pet.memory.cells.uint32,
        pet.memory.cells.int64,
        pet.memory.cells.uint64,
    ]


# end of file
