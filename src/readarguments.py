# Default and user inputs for GeoPlot

# import dependencies
import argparse
from pathlib import Path
import sys
import re

# Add the path to the root of the project to sys.path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


# All functions related to importing the topographic map
class ReadArguments:
    def __init__(self):
        self = self

    # Helper function to define coordinate type
    def coords_split(self, s):
        seps = r"[ ]"
        try:
            situp = []
            for si in re.split(seps, s):
                situp.append(tuple(map(float, si.split(","))))
            return situp
        except:
            raise argparse.ArgumentTypeError(
                "Coordinates must be given divided by commas and space, dot, or semicolon e.g.: 'x,y k,l'"
            )

    # Read arguments supplied in the command line
    def get_args(self) -> argparse.Namespace:
        """Get arguments

        Returns
        -------
        args : argparse.Namespace
            Argument values
        """
        description = "Plot sample locations on a topographic map"
        parser = argparse.ArgumentParser(description=description, add_help=False)
        parser.add_argument(
            "-i",
            "--indir",
            required=True,
            type=Path,
            help="Directory containing raster files to create the map (*.tif), \
            (optional) a shape file to mask the map (*.shp), and the sample information \
            in a tab delimited file (*.yaml|*.txt).",
            metavar="INDIR",
        )
        default_mode = "./figures"
        parser.add_argument(
            "-o",
            "--outdir",
            type=Path,
            default=default_mode,
            help='Output directory where final figures will be saved. Default: "./figures"',
            metavar="OUTDIR",
        )
        parser.add_argument(
            "-m",
            "--mask",
            type=str,
            required=True,
            help="Choose the method to determine the final map shape ('country'|'coords')",
            choices=["country", "coords"],
            metavar="MASK",
        )
        parser.add_argument(
            "-c",
            "--country",
            type=str,
            required=False,
            help="Name of the country shape to be used. Required if --mask country is chosen.",
            metavar="COUNTRY",
        )
        parser.add_argument(
            "-coords",
            "--coordinates",
            required=False,
            type=self.coords_split,
            help="Geographic coordinates (WGS84) in decimal degrees of a bounding box to be used to \
                select the desired part of the map. Coordinates should be provided as a set \
                for the lower left corner, and a set for the upper right corner of the box \
                separated by a space. \
                Like: ('minimum latitude','minimum longitude' 'max latitude','minimum longitude') | ('0,0 45,45').",
        )
        default_mode = int(0)
        parser.add_argument(
            "-nd",
            "--no_data_value",
            type=int,
            default=default_mode,
            help="Raster pixel values to be set to 'nodata'. Default is int(0) that corresponds to sea level pixels.",
            nargs=1,
            metavar=(range(0 - 255)),
        )
        default_mode = "gray"
        parser.add_argument(
            "-cm",
            "--colourmap",
            type=str,
            default=default_mode,
            help="A colour gradient selected from Matplotlib's colourmaps. \
                Found here: https://matplotlib.org/stable/users/explain/colors/colormaps.html \
                The name of the colour gradient should be provided like: 'viridis' \
                Default: 'gray'",
            nargs=1,
            metavar=("COLOURMAP"),
        )
        default_mode = (7, 3.5)
        parser.add_argument(
            "-size",
            "--figure_size",
            type=int,
            default=default_mode,
            help="The length and width of the final figure in inches. \
                Default: length = 7 inches, width = 3.5 inches (7,3.5)",
            nargs=2,
            metavar=("length", "width"),
        )
        default_mode = int(1)
        parser.add_argument(
            "-alt",
            "--altitude",
            type=int,
            default=default_mode,
            help="Value between 1 and 90 that determines the altitude of the light source. \
                The lower the value, the more exaggerated the shadow will be. Default: 1",
            choices=range(1, 90),
            metavar="[1-90]",
        )
        default_mode = int(180)
        parser.add_argument(
            "-azi",
            "--azimuth",
            type=int,
            default=default_mode,
            help="Value between 0 and 360 that determines the angular distance from due north \
                where the light source will come from. A value of 0 corresponds to a light \
                source pointing due north. Default: 180",
            choices=range(0, 360),
            metavar="[0-360]",
        )
        args = parser.parse_args()
        return args
