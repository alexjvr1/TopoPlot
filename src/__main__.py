##TopoPlot##


# Import modules and initiate instances of each class
from readarguments import ReadArguments
from importmap import ImportMap

# from colourmap import ColourMap
# from samplestomap import SamplesToMap

ReadArguments = ReadArguments()
ImportMap = ImportMap()
# ColourMap = ColourMap()
# SamplesToMap = SamplesToMap()

# Import all arguments.
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
outdir.mkdir(exist_ok=True)
# Import raster file and return the 'mosaic' variable of all the tiles stitched together
# Save mosaic.tif, and save a plot (.png) of the mosaic map to the output folder
# Options: raster dir, outdir

mosaic = ImportMap.import_and_merge_raster_file(
    path_to_raster=args.indir, outdir=args.outdir
)

# Create a mask to delimit the map (ImportMap)
# If --country option is selected:
if args.mask == "country":
    # Use function to produce a country mask
    ImportMap.mask_map_by_country(
        indir=args.indir, country=args.country, outdir=args.outdir
    )
    # Else coordinates are selected
elif args.mask == "coords":
    print("Coordinates chosen")
# ImportMap.mask_map_by_coords(args.coords)
# Use function to use coordinates to create mask
# Save figure (.png)
# Return mask variable


# main()

# Function to readjust the scale (ColourMap)

# Function to colour the map using different colour palettes (default grey scale)
# ColourMap

# Import samples and plot
# SamplesToMap
# Variables: colour, size, shape, population (for legend)
# Default: black, small, circles, one population
# Print figure (default .png), optional pdf


# def execute_main():
#    if __name__ == "__main__":
#        execute_main()
