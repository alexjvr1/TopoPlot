# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import ListedColormap
import earthpy.spatial as es
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import pickle


# All functions related to colouring and adding a light source to the map
class ColourMap:
    def __init__(self):
        self = self

    # Create a map with a colour gradient representing the range in elevation values for our map
    def map_in_colour(
        self,
        colourgrad,
        value_range,
        clipped_array,
        azimuth,
        altitude,
        fig_height,
        fig_width,
        outdir,
    ):
        # Rescale the colourgradient to the value_range
        colourgrad = mpl.colormaps[str(colourgrad)].resampled(value_range)
        newcolours = colourgrad(np.linspace(0, 1, 256))
        # Add background colour: white
        background_colour_white = np.array([255 / 255, 255 / 255, 255 / 255, 1.0])
        newcolours = np.vstack((newcolours, background_colour_white))
        # create the final colour gradient
        map_colourgrad = ListedColormap(newcolours)
        # Define hillshade
        hillshade = es.hillshade(clipped_array[0], azimuth, altitude)
        # plot the figure
        fig, ax = plt.subplots()
        fig.set_size_inches(int(fig_width), int(fig_height))
        plt.imshow(clipped_array[0], cmap=map_colourgrad, norm=colors.LogNorm())
        ax.imshow(hillshade, cmap="Greys", alpha=0.3)
        ax.axis("off")
        newax = fig.add_axes([0.79, 0.78, 0.08, 0.08], anchor="NE")
        newax.axis("off")
        output_path = str(str(outdir) + "/colourmap")
        plt.savefig(output_path + ".png")
        plt.savefig(output_path + ".pdf")
        pickle.dump(ax, open("myplot.pickle", "wb"))

    # Read in sample and location information
    def read_sample_info(self, sample_indir, sample_data):
        # Read data from a tab delimited file
        path_to_data = str(str(sample_indir) + "/" + sample_data)
        data = np.genfromtxt(path_to_data, delimiter="\t")
        print(data)
        return data

    # Plot sample locations on the colour map
    def map_samples(
        self, input, samples, marker_size, marker_colour, marker_style, alpha
    ):
        # Load map from pickled colour map saved with map_in_colour()
        fig_handle = pickle.load(open("myplot.pickle", "rb"))
        fig_handle.pyplot.scatter()
        ax.scatter()
        ax.set_xlabel("Latitude")
        ax.set_ylabel("Longitude")
        # sample_df = pd.read_table((str(input) + "/" + samples))
        # Lat =
        # Long =
        # geometry = [Point(xy) for xy in zip(sample_df["Long"], sample_df["Lat"])]
        # gdf = GeoDataFrame(sample_df, geometry=geometry)
        # gdf.plot(ax=ax, marker="o", color="red", markersize=15)
        # plt.show()
        # return fig, ax
