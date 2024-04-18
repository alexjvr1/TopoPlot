##GeoPlot##

# Import dependencies
import argparse
from pathlib import Path
import sys


# Add the path to the root of the project to sys.path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

# Define variables
path_to_raster = "example/"

# Import modules and initiate instances of each class
from importmap import ImportMap


ImportMap = ImportMap()


# Import raster file and create mosaic
mosaic = ImportMap.import_and_merge_raster_file(path_to_raster)


##Plot samples on topographic maps


# def execute_main():
#   if __name__ == "__main__":  # Condition to ensure module is executed not imported.
#       execute_main()
