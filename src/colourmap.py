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


# All functions related to colouring and adding a light source to the map
class ColourMap:
    def __init__(self):
        self = self

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
        fig_height,
        fig_width,
        map_extent,
        outdir,
        sample_indir,
        sample_data,
        plotdata,
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
        # set variables
        map_extent = map_extent
        # plot the figure
        fig, ax = plt.subplots()
        fig.set_size_inches(int(fig_width), int(fig_height))
        ax.imshow(
            clipped_array[0],
            cmap=map_colourgrad,
            norm=colors.LogNorm(),
            extent=map_extent,
            zorder=1,
        )
        # ax.axes(projection=ccrs.PlateCarree())
        ax.imshow(hillshade, cmap="Greys", alpha=0.3, extent=map_extent, zorder=0)
        ax.axis("on")
        # newax = fig.add_axes([0.79, 0.78, 0.08, 0.08], anchor="NE")
        # newax.axis("off")
        output_path = str(str(outdir) + "/colourmap")
        # if/elif/else statement for plotting scatter plot based on user specified marker and colour, or default values
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
            plt.savefig("test.png")
            plt.show()
        # If colour and marker is not assigned, plot in black and randomly assign marker shape
        else:
            # Read in data file containing Population, Lat, and Long
            path_to_data = str(str(sample_indir) + "/" + sample_data)
            data = pd.read_csv(path_to_data, delimiter="\t", header=0)
            # Get list of population names
            pop = data.Population.unique()
            # hex values to create a random colour for each population
            hexadecimal_alphabets = "0123456789ABCDEF"
            # generate a random hex colour for each population
            color = [
                "#" + "".join([random.choice(hexadecimal_alphabets) for j in range(6)])
                for i in pop
            ]
            # create a dictionary of population names and random colours
            colour_dict = dict(zip(pop, color))
            # Group data by population
            for name, group in data.groupby("Population"):
                group = group.copy()
                ax.scatter(
                    x=group["Long"],
                    y=group["Lat"],
                    marker="o",
                    # Assign colour by referring to colour dictionary
                    color=group["Population"].map(colour_dict),
                    # assign label name for legend
                    label=name,
                    zorder=2,
                )
                # Plot legend in the upper right corner
                ax.legend(loc="upper right")
            plt.savefig("test.png")
            plt.show()
        # plt.savefig(output_path + ".png")
        # plt.savefig(output_path + ".pdf")
        # pickle.dump(ax, open("myplot.pickle", "wb"))
        return map
        # plt.savefig(output_path + ".png")
        # plt.savefig(output_path + ".pdf")
        # pickle.dump(ax, open("myplot.pickle", "wb"))
        return map

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
