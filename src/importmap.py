# Functions to import a topographic map using Python
# and create a map to the required extent

# import all dependencies
import rasterio
from rasterio import mask
from rasterio.merge import merge
import matplotlib.pyplot as plt
from pathlib import Path
import geopandas as gpd
from shapely.geometry import Polygon
from shapely.geometry import mapping
import glob
import numpy as np
import pyshp


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

    # Helper function to clip raster using a polygon, and to assign the nodata
    # cells to the max(polygon) value + 1 so that there is no natural gap in
    # the value range.
    def clip_raster(self, path_to_mosaic, polygon):
        with rasterio.open(path_to_mosaic) as raster:
            out_image, out_transform = rasterio.mask.mask(
                raster, [mapping(polygon.iloc[0].geometry)], crop=True
            )
            out_image, out_transform = rasterio.mask.mask(
                raster,
                [mapping(polygon.iloc[0].geometry)],
                crop=True,
                nodata=(np.amax(out_image[0]) + 1),
            )
            out_meta = raster.meta
            out_meta.update(
                {
                    "driver": "GTiff",
                    "height": out_image.shape[1],
                    "width": out_image.shape[2],
                    "transform": out_transform,
                }
            )
            out_image[0] = out_image[0] + abs(np.amin(out_image))
            value_range = np.amax(out_image) + abs(np.amin(out_image))
            return out_image, value_range, out_meta

    # Mask map according to country shape
    # outdir is the directory where the input raster is saved after merge
    # by import_and_merge_raster_file
    # This is also the directory where the masked output map will
    # be saved
    def mask_map_by_country(self, indir, country, outdir):
        path = indir
        output_path = outdir
        country = country
        shape_file = self.find_file_in_posixpath(path, "*shp")
        shapefile = gpd.read_file(shape_file)
        country = shapefile.loc[shapefile["ADMIN"] == country]
        path_to_mosaic = self.find_file_in_posixpath(output_path, "*tif")
        # Helper function to clip the raster
        out_image, value_range, out_meta = self.clip_raster(
            path_to_mosaic, polygon=country
        )
        output_path = str(str(outdir) + "/mosaic.masked.tif")
        with rasterio.open(output_path, "w", **out_meta) as dest:
            dest.write(out_image)
        plt.imshow(out_image[0], cmap="Spectral")
        plt.savefig(output_path + ".png")
        return out_image, value_range

    # Helper function to create a bounding box based on coordinates and write a shapefile
    def bbox(self, coords, outdir):
        coords_tuple = tuple(np.array(coords).ravel())
        lat0 = coords_tuple[0]
        long0 = coords_tuple[1]
        lat1 = coords_tuple[2]
        long1 = coords_tuple[3]
        #polygon = Polygon([[lat0, long0], [lat1, long0], [long1, lat1], [long0, lat1]])
        bbox = shapefile.Writer(shapefile.POLYGON)
        bbox.poly(parts=[[[lat0, long0], [lat1, long0], [long1, lat1], [long0, lat1]]]) 
        bbox.field('FIRST_FLD','C','40') 
        bbox.field('SECOND_FLD','C','40') 
        bbox.record('First','Polygon') 
        outdir = str(outdir + 'polygon.shp')
        bbox.save(outdir)
        return polygon

    # Mask map according to user defined shape
    def mask_map_by_coords(self, map, polygon):
        