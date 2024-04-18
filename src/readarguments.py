# Default and user inputs for GeoPlot

# import dependencies
import argparse
from pathlib import Path
import sys


# Add the path to the root of the project to sys.path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


# All functions related to importing the topographic map
class ReadArguments:
    def __init__(self):
        self = self

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
            required=True,
            help="Name of the country shape to be used. Required if --mask country is chosen.",
            metavar="COUNTRY",
        )
        args = parser.parse_args()
        return args
