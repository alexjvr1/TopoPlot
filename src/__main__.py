##TopoPlot##


# Define variables
path_to_raster = "example/"

# Import modules and initiate instances of each class
# from readarguments import ReadArguments
from importmap import ImportMap

# from colourmap import ColourMap
# from samplestomap import SamplesToMap

# ReadArguments = ReadArguments()
ImportMap = ImportMap()
# ColourMap = ColourMap()
# SamplesToMap = SamplesToMap()


# TopoMap main function for entry point
def main():
    # Import all arguments. Now we can call the arguments as args.argument
    args = ReadArguments.getargs()
    # Import raster file and return the 'mosaic' variable of all the tiles stitched together
    # Save mosaic.tif, and save a plot (.png) of the mosaic map to the output folder
    # Options: raster dir, outdir
    mosaic = ImportMap.import_and_merge_raster_file(path_to_raster)

    # Create a mask to delimit the map (ImportMap)
    # If --country option is selected:
    if args.mask == 'country': 
        # Use function to produce a country mask
        ImportMap.mask_map_by_country(args.mask)
    # Else coordinates are selected
    else args.mask == 'coords':
        ImportMap.mask_map_by_coords(args.coords)
        # Use function to use coordinates to create mask
    # Save figure (.png)
    # Return mask variable

    # Function to readjust the scale (ColourMap)

    # Function to colour the map using different colour palettes (default grey scale)
    # ColourMap

    # Import samples and plot
    # SamplesToMap
    # Variables: colour, size, shape, population (for legend)
    # Default: black, small, circles, one population
    # Print figure (default .png), optional pdf


def execute_main():
    if __name__ == "__main__":
        execute_main()
