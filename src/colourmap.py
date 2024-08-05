# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import colors
from matplotlib.colors import ListedColormap
import earthpy.spatial as es
import pandas as pd
import pickle
import random


# All functions related to plotting colour map with scatter plot of sample locations layered on top
class ColourMap:
    def __init__(self):
        self = self

    # Helper functions:
    # Helper function to create colourgradient scaled to the value range as determined by \
    # the elevational scale
    # Rescale the colourgradient to the value_range
    def create_colourgrad(self, colourgrad, value_range):
        colourgrad = mpl.colormaps[colourgrad].resampled(value_range)
        newcolours = colourgrad(np.linspace(0, 1, 256))
        # Add background colour: white
        background_colour_white = np.array([255 / 255, 255 / 255, 255 / 255, 1.0])
        newcolours = np.vstack((newcolours, background_colour_white))
        # create the final colour gradient
        map_colourgrad = ListedColormap(newcolours)
        return map_colourgrad

    # Helper function to read data from a csv file and return data, and dictionaries of \
    # pop:colour and pop:marker
    def read_data_for_scatter_plot(
        self,
        sample_indir,
        sample_data,
    ):
        # Read data from a tab delimited file
        path_to_data = str(str(sample_indir) + "/" + sample_data)
        data = pd.read_csv(path_to_data, delimiter="\t", header=0)
        # Create a dictionary based on the Population and Colour columns
        colour_dict = dict(zip(data.Population, data.Colour))
        # Create a dictionary based on the Population and Shape columns
        marker_dict = dict(zip(data.Population, data.Marker))
        return data, colour_dict, marker_dict

    # Create a map with a colour gradient representing the range in elevation values for our map
    def map_in_colour(
        self,
        colourgrad,
        value_range,
        clipped_array,
        azimuth,
        altitude,
        alpha,
        fig_height,
        fig_width,
        map_extent,
        outdir,
        sample_indir,
        sample_data,
        plotdata,
        maptitle,
    ):
        # Rescale the chosen colour gradient to the elevational value_range
        map_colourgrad = self.create_colourgrad(colourgrad, value_range)
        # set variables
        map_extent = map_extent
        alpha = alpha
        # Define hillshade
        hillshade = es.hillshade(clipped_array[0], azimuth, altitude)
        # plot the figure
        fig, ax = plt.subplots()
        fig.set_size_inches(int(fig_width), int(fig_height))
        # Layer 1:colour relief map
        ax.imshow(
            clipped_array[0],
            cmap=map_colourgrad,
            norm=colors.LogNorm(),
            extent=map_extent,
            zorder=0,
        )
        # Layer 2: Add hillshade
        ax.imshow(hillshade, cmap="Greys", alpha=alpha, extent=map_extent, zorder=1)
        ax.axis("on")
        # output_path = str(str(outdir) + "/colourmap")
        # Layer 3: Plot samples
        # if/else statement for plotting scatter plot based on user specified marker \
        # and colour, or default values
        if plotdata == "True":
            # read data in
            data, colour_dict, marker_dict = self.read_data_for_scatter_plot(
                sample_indir, sample_data
            )
            # Group data by population
            for name, group in data.groupby("Population"):
                group = group.copy()
                # marker assigned to each population
                markers = marker_dict.get(name)
                # Create scatter plot and assign marker based on population group.
                ax.scatter(
                    x=group["Long"],
                    y=group["Lat"],
                    marker=markers,
                    # Assign colour by referring to colour dictionary
                    color=group["Population"].map(colour_dict),
                    # assign label name for legend
                    label=name,
                    zorder=2,
                )
                # Plot legend in the upper right corner
                ax.legend(loc="upper right")
            plt.title(maptitle)
            output_path = str(str(outdir) + "/FinalMap")
            plt.savefig(output_path + ".png")
            plt.savefig(output_path + ".pdf")
            plt.show()
        # If colour and marker is not assigned, plot circle and randomly assign marker colour
        else:
            # Read in data file containing Population, Lat, and Long
            path_to_data = str(str(sample_indir) + "/" + sample_data)
            data = pd.read_csv(path_to_data, delimiter="\t", header=0)
            # Get list of population names
            pop = data["Population"].unique()

            # Create a list of valid symbols from matplotlib
            marker_symbols = [
                ".",
                "o",
                "v",
                "^",
                "<",
                ">",
                "s",
                "p",
                "P",
                "*",
                "h",
                "x",
                "X",
                "D",
                "d",
            ]
            # generate a random marker for each population
            marker = [random.choice(marker_symbols) for i in pop]
            # create a dictionary of population names and random markers
            marker_dict = dict(zip(pop, marker))
            # Group data by population
            for name, group in data.groupby("Population"):
                group = group.copy()
                # Assign marker by referring ot the marker dictionary
                marker = marker_dict.get(name)
                ax.scatter(
                    x=group["Long"],
                    y=group["Lat"],
                    color="k",
                    marker=marker,
                    # assign label name for legend
                    label=name,
                    zorder=2,
                )
                # Plot legend in the upper right corner
                ax.legend(loc="upper right")
            plt.title(maptitle)
            output_path = str(str(outdir) + "/FinalMap")
            plt.savefig(output_path + ".png")
            plt.savefig(output_path + ".pdf")
            plt.show()
        return map
