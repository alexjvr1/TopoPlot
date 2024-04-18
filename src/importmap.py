# Functions to import a topographic map using Python
# and create a map to the required extent

# import all dependencies
import rasterio
from rasterio.merge import merge
import matplotlib.pyplot as plt
from pathlib import Path
import geopandas as gpd
from shapely.geometry import mapping
from rasterio import mask


# All functions related to importing the topographic map
class ImportMap:
    def __init__(self):
        self = self

    # Read elevation datasets into Python and return as object
    def import_and_merge_raster_file(self, path_to_raster):
        path = Path(path_to_raster)
        # Create an output folder for the mosaic raster
        Path("output").mkdir(parents=True, exist_ok=True)
        output_path = "output/mosaic_output.tif"
        # Read in all the rasters
        raster_files = list(path.iterdir())
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
    def mask_map_by_country(self, country):
        country = country


df = gpd.read_file("NaturalEarth/data/10m_cultural/ne_10m_admin_0_countries.shp")

italy = df.loc[df["ADMIN"] == "Italy"]

clipped_array, clipped_transform = msk.mask(
    file, [mapping(italy.iloc[0].geometry)], crop=True
)

plt.imshow(clipped_array[0], cmap="Spectral")
plt.show()


# Mask map according to user defined shape

# Mask map according to user defined shape
