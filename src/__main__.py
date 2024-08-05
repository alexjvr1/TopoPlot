##TopoPlot##


# Import modules and initiate instances of each class
from readarguments import ReadArguments
from importmap import ImportMap
from colourmap import ColourMap

ReadArguments = ReadArguments()
ImportMap = ImportMap()
ColourMap = ColourMap()

# Import all arguments supplied by user, otherwise use defaults.
args = ReadArguments.get_args()
print(args)

# Check that country is selected if we're using a shape file to mask the map
if args.mask == "country" and args.country is None:
    parser.error(
        "if --mask country is chosen, a country name needs to be provided with --country"
    )


# TopoMap main function for entry point
# def main():
# make the outdir if needed
outdir = args.outdir
print("Creating", outdir, "if it does not exist.")
outdir.mkdir(exist_ok=True)


################################################################
# Part 1: Create a mosaic raster using the input raster files #
################################################################
# Import raster file and return the 'mosaic' variable of all the tiles stitched together
# Save mosaic.tif, and save a plot (.png) of the mosaic map to the output folder
print("Import raster files to merge")
mosaic = ImportMap.import_and_merge_raster_file(
    path_to_raster=args.indir, outdir=args.outdir
)
print("Merged raster file (*.tif) and figure (*.png) saved to", outdir)


####################################################################
# Part 2: Mask the mosaic raster using country and/or coordinates #
####################################################################
# Choose from three options to mask the raster file according to the required \
# shape or coordinates.

# Option 1 (--country + --coordinates):
# Create a mask to crop the map and show only the region of interest (ImportMap)
# If --country option is selected:
if args.mask == "country" and bool(args.coordinates) == True:
    # Use function to clip map by country mask. Return the masked image and a
    # value range for the elevation assigned to each cell in the map
    print(
        "Clipping raster with mask for",
        args.country,
        "and clip map to include only",
        args.coordinates,
    )
    out_img, value_range = ImportMap.mask_map_by_country(
        indir=args.indir, country=args.country, outdir=args.outdir
    )
    print("Clipped", args.country, "raster (*.tif) and figure (*.png) saved to", outdir)

    # Write bounding box polygon to shapefile
    polygon = ImportMap.bbox(coords=args.coordinates)

    # write polygon to shape file in outdir
    ImportMap.write_bbox_to_shp(polygon=polygon, outdir=args.outdir)

    # Mask map with the polygon
    ##Find the masked map
    path_to_map = ImportMap.find_file_in_posixpath(args.outdir, "*masked.tif")
    out_img, value_range = ImportMap.mask_map_by_polygon(
        path_to_map=path_to_map, path_to_polygon=args.outdir, outdir=args.outdir
    )
    print(
        "Clipped",
        args.country,
        "raster (*.tif) using the bounding box",
        args.coordinates,
    )

    # create map_extent variable to be used in Part2
    map_extent = ImportMap.define_map_extent(coords=args.coordinates)
    print("map extent is:", map_extent)


# Option2 (--country):
# Plot a map of the country without further clipping
elif args.mask == "country" and bool(args.coordinates) == False:
    print("Clipping raster with mask for", args.country)
    out_img, value_range = ImportMap.mask_map_by_country(
        indir=args.indir, country=args.country, outdir=args.outdir
    )
    print(
        "Clipped",
        args.country,
        "raster (*.tif) and figure (*.png) saved to",
        args.outdir,
    )

    # create map_extent variable to be used in Part2
    map_extent = ImportMap.define_map_extent_from_tif(
        geotiff="output/FINAL.clipped.tif"
    )
    print("map extent is:", map_extent)

# Option 3 (--coordinates):
# Mask the map using the bounding box created by the coordinates only.
elif args.mask == "coords" and bool(args.country) == False:
    print("Clip map by coordinates")

    # Create polygon from coordinates
    polygon = ImportMap.bbox(coords=args.coordinates)
    # write polygon to shape file in outdir
    ImportMap.write_bbox_to_shp(polygon=polygon, outdir=args.outdir)

    ##Find the mosaic map
    path_to_map = ImportMap.find_file_in_posixpath(args.outdir, "mosaic_output.tif")

    # Set pixel values of 0 to 'nodata' so that sea level pixels have a big colour contrast with the land data.
    output_file = ImportMap.find_file_in_posixpath(args.outdir, "mosaic_output.tif")
    ImportMap.fix_no_data_value(
        path_to_map, output_file, no_data_value=args.no_data_value
    )

    # Mask map with the polygon
    out_img, value_range = ImportMap.mask_map_by_polygon(
        path_to_map=path_to_map, path_to_polygon=args.outdir, outdir=args.outdir
    )
    print(
        "Clipped raster (*.tif) using the bounding box",
        args.coordinates,
    )

    # create map_extent variable to be used in Part2
    map_extent = ImportMap.define_map_extent(coords=args.coordinates)
    print("map extent is:", map_extent)


# If neither coordinates or country name are provided:
else:
    print(
        "Cannot create a mask for the map. \
        --coordinates and/or --country are required arguments"
    )

###########################################
# Part 2: Plot the colour map and samples #
###########################################

ColourMap.map_in_colour(
    colourgrad=args.colourmap,
    value_range=value_range,
    clipped_array=out_img,
    azimuth=args.azimuth,
    alpha=args.alpha,
    altitude=args.altitude,
    fig_height=args.figureheight,
    fig_width=args.figurewidth,
    map_extent=map_extent,
    outdir=args.outdir,
    sample_indir=args.sample_dir,
    sample_data=args.sample_data,
    plotdata=args.plotdata,
    maptitle=args.maptitle,
)


# def execute_main():
#    if __name__ == "__main__":
#        execute_main()
