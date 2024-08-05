# TopoPlot
Create beautiful topographic maps with of sample locations.

TopoPlot is an easy to use tool to create topographic maps of any region of the world using either country names, or specific coordinates. The map is coloured by elevation, and can be customised using any of the colourgradients available in matplotlib. Sample or population coordinates are plotted on top of the topographic map. These are plotted in black by default with a random marker shape assigned for each population, or they can be customised with a user provided input file. 

## Requirements

1. Topographic data: A raster file containing elevational data for the region of interest. See our suggestion [here](https://github.com/alexjvr1/TopoPlot/blob/main/README.md#topographic-data) 

2. Bounds for the map: Either coordinates (best if you're mapping a specific area) or a shape file (best if you're mapping a country or state). See our suggestion [here](https://github.com/alexjvr1/TopoPlot/blob/main/README.md#shape-file-for-map-mask---mask-country)

3. Sample data: A tab delimited file with the following columns with at least Population, Lat, and Long as columns. Optionally, Colour and Marker can be provided to customise sample points. Column order does not matter.

|Population|Lat|Long|Colour|Marker|
|----------|--------|---------|------|------|
|Pop1 |51.338404 |-0.12074935 |^ |goldenrod|
|Pop1 |51.314844 |-0.1661964 |^ |goldenrod|
|Pop2 |51.299128 |-0.029111665 |s |seagreen|
|Pop2 |51.439448 |-0.45041888 |s |blue|
|Pop3 |53.474438 |-0.98750698 |s |blue|
|Pop3 |53.474438 |-0.98750698 |s |seagreen|

## Quick start

Python3+ is required. 

Install bioconda package: 
```
conda install -c conda-forge -c bioconda topomap
```

Install PyPI stable package:
```
pip install topomap
```

### Topographic data
TopoPlot requires elevation data in raster format for the area to be plotted. We suggest you use the Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010) that contains elevation data for the globe collected from various sources at 7.5 arc-seconds resolution. More information on the dataset can be found [here](https://topotools.cr.usgs.gov/GMTED_viewer/gmted2010_fgdc_metadata.html)

The required grid square(s) can be downloaded from the USGS following [this link](https://topotools.cr.usgs.gov/gmted_viewer/viewer.htm). 

1) Select the grid square(s) you're interested in.

2) Click on the folder for the grid square and select the resolution you'd like to use. The example dataset uses the "Systematic Subsample - 7.5 arc-sec" resolution.

3) Download the files and move them into a folder in the project directory (default expected: raster)

4) Suggested citation: Danielson, J.J., and Gesch, D.B., 2011, Global multi-resolution terrain elevation data 2010 (GMTED2010): U.S. Geo- logical Survey Open-File Report 2011–1073, 26 p.


### Shape file for map mask: '--mask country'
To extract the part of the map that is of interest, TopoMap makes use either of a set of coordinates (see below), or a polygon in the shape of the country of interest. 

Natural Earth Data provides one such source of shape files for countries. Different versions of these (varying by how borders are defined) can be downloaded [here](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/). If using this shapefile, country names should be provided in full (e.g. "United Kingdom"). A list of the available countries is provided with the shapefile in TopoMap/example_data.

They can also be downloaded per country from the GADM [here](https://gadm.org/download_country.html), but these files are MUCH larger. 

To supply a custom polygon, use the '--mask country' option and simply provide a custom shape file.  


### Coordinates for map mask: '--mask coords'



### Options for hillshade aesthetics



#### altitude


#### azimuth


# default: 


### Sample data


<<<<<<< HEAD
### Options for plotting markers

#### Shape

A full list of the available markers can be found in the matplotlib documentation [here](https://matplotlib.org/1.4.1/api/markers_api.html). The most commonly used markers are: 

#TODO add figure of markers


#### Colour

=======
Coordinates

Colour from the [available list](https://matplotlib.org/stable/gallery/color/named_colors.html)

Marker shape from the [available list](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers)
>>>>>>> 21887a8f72d9cd17595923e0d1264abfaefc3c9d
