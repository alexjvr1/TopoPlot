# Functions to import a topographic map using Python
# and create a map to the required extent

# import all dependencies
import rasterio
from rasterio import mask
from rasterio.merge import merge
import matplotlib.pyplot as plt
from pathlib import Path
import geopandas as gpd
from shapely.geometry import mapping
import glob
import fiona


# All functions related to importing the topographic map
class ImportMap:
    def __init__(self):
        self = self

    # Helper function to find the path to a single file with a particular
    # file extension in a posix.Path
    def find_file_in_posixpath(self, posixpath, file_extension):
        path = Path(posixpath)
        file_extension = str(file_extension)
        path_to_file = str(Path.joinpath(path, file_extension))
        path_to_file = glob.glob(path_to_file)
        path_to_file = path_to_file[0]
        return path_to_file

    # Read elevation datasets into Python and return as object
    def import_and_merge_raster_file(self, path_to_raster, outdir):
        path = Path(path_to_raster)
        # Create an output folder for the mosaic raster
        Path(outdir).mkdir(parents=True, exist_ok=True)
        output_path = "output/mosaic_output.tif"
        # Read in all the rasters
        raster_files = list(path.glob("*.tif"))
        raster_to_mosiac = []
        # loop through files and create a list of raster files to merge
        for p in raster_files:
            raster = rasterio.open(p)
            raster_to_mosiac.append(raster)
        # merge all the rasters
        mosaic, output = merge(raster_to_mosiac)
        # update the mosaic raster's metadata to match the new height and width
        output_meta = raster.meta.copy()
        output_meta.update(
            {
                "driver": "GTiff",
                "height": mosaic.shape[1],
                "width": mosaic.shape[2],
                "transform": output,
            }
        )
        # write the mosaic file to the output directory
        with rasterio.open(output_path, "w", **output_meta) as m:
            m.write(mosaic)
        # plot the mosaic file to check that the area we need is covered by the map
        plt.imshow(mosaic[0], cmap="Spectral")
        plt.savefig(output_path + ".png")
        # return the mosaic as an object
        return mosaic

    # Mask map according to country shape
    # outdir is the directory where the input raster is saved after merge \
    # by import_and_merge_raster_file
    # This is also the directory where the masked output map will
    # be saved
    def mask_map_by_country(self, indir, country, outdir):
        path = indir
        output_path = outdir
        country = country
        shape_file = self.find_file_in_posixpath(path, "*shp")
        df = gpd.read_file(shape_file)
        country = df.loc[df["ADMIN"] == country]
        path_to_mosaic = self.find_file_in_posixpath(output_path, "*tif")
        #
        with rasterio.open(path_to_mosaic) as raster:
            clipped_array, clipped_transform = rasterio.mask.mask(
                raster, [mapping(country.iloc[0].geometry)], crop=True
            )
        plt.imshow(clipped_array[0], cmap="Spectral")
        plt.savefig(Path.joinpath(output_path, ".png"))
        return clipped_array

    # Mask map according to user defined shape
    def mask_map_by_coords(self, lat, long):
        lat = lat
        long = long
