# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import ListedColormap
import earthpy.spatial as es


# All functions related to colouring and adding a light source to the map
class ColourMap:
    def __init__(self):
        self = self

    def plot_examples(self, colormaps):
        # From Matplotlib documentation:
        # Helper function to plot data with associated colormap.
        np.random.seed(19680801)
        data = np.random.randn(30, 30)
        n = len(colormaps)
        fig, axs = plt.subplots(
            1, n, figsize=(n * 2 + 2, 3), layout="constrained", squeeze=False
        )
        for [ax, cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
            fig.colorbar(psm, ax=ax)
        plt.show()

    # representing the range in elevation values for our map
    def map_in_colour(self, colourgrad, value_range, clipped_array, azimuth, altitude):
        # Rescale the colourgradient to the value_range
        colourgrad = mpl.colormaps[str(colourgrad)].resampled(value_range)
        newcolours = colourgrad(np.linspace(0, 1, 256))
        background_colour_white = np.array([255 / 255, 255 / 255, 255 / 255, 1.0])
        newcolours = np.vstack((newcolours, background_colour_white))
        map_colourgrad = ListedColormap(newcolours)
        """ # Plot
        fig = plt.figure(facecolor="#FCF6F5FF")
        fig.set_size_inches(7, 3.5)
        ax = plt.axes()
        plt.imshow(clipped_array[0], cmap=map_colourgrad)
        ax.axis("off")
        plt.show() """
        hillshade = es.hillshade(clipped_array[0], azimuth, altitude)
        fig, ax = plt.subplots()
        fig.set_size_inches(5, 5)
        i = plt.imshow(clipped_array[0], cmap=map_colourgrad, norm=colors.LogNorm())
        ax.imshow(hillshade, cmap="Greys", alpha=0.3)
        ax.axis("off")
        newax = fig.add_axes([0.79, 0.78, 0.08, 0.08], anchor="NE")
        newax.axis("off")
        plt.show()

    # and hillshade to the topography map

    # Define the colour scale for the map

    # Add hillshade to the map
    def plot_hillshade(self, altitude, azimuth):
        alt = altitude
        azi = azimuth
        return alt, azi
