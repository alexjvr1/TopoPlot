# Default and user inputs for GeoPlot

# import dependencies
import argparse
from pathlib import Path


# Read arguments supplied in the command line
def get_args() -> argparse.Namespace:
    """Get arguments

    Returns
    -------
    args : argparse.Namespace
        Argument values
    """
    description = "Plot sample locations on a topographic map"
    parser = argparse.ArgumentParser(description=description, add_help=False)

    parser.add_argument(
        "-r",
        "--raster_indir",
        required=True,
        type=Path,
        help="Directory containing raster files to create the map (*.tif)",
        metavar="RASTER",
    )
    parser.add_argument(
        "-i",
        "--indir",
        required=True,
        type=Path,
        help="Directory containing sample information in tab delimited file (*.yaml|*.txt)",
        metavar="DATA",
    )
    default_mode = "figures"
    parser.add_argument(
        "-o",
        "--outdir",
        required=True,
        type=Path,
        help="Output directory where final figures will be saved",
        metavar="OUTDIR",
    )
    default_mode = "fastani"
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        help="ANI calculation mode ('fastani'[default]|'skani')",
        default=default_mode,
        choices=["fastani", "skani"],
        metavar="",
    )
    args = parser.parse_args()
    return args
