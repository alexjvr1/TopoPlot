# TopoPlot
Plot sample points on a topographical map. 

TopoPlot plots sample locations on topographical maps. The default maps are in grey scale, or the map can be produced in a custom colour palette. Sample colour, shape, and size can be chosen by the user. 

## Requirements

1. Topographic data. See our suggestion [here]() 

2. Coordinates (best if you're mapping a specific area) or a shape file (best if you're mapping a country or state). See our suggestion [here]()

3. A tab delimited file containing sample/population names, latitude, longitude, and (optional) colour, shape, and size of the points to be plotted. See our example [here]()


## Quick start

Install TopoMap 
```
```

### Topographic data
TopoPlot requires elevation data in raster format for the area to be plotted. We use the Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010) that contains elevation data for the globe collected from various sources at 7.5 arc-seconds resolution. More information on the dataset can be found [here](https://topotools.cr.usgs.gov/GMTED_viewer/gmted2010_fgdc_metadata.html)

The required grid square(s) can be downloaded from the USGS following [this link](https://topotools.cr.usgs.gov/gmted_viewer/viewer.htm). 

1) Select the grid square(s) you're interested in.

2) Click on the folder for the grid square and select the resolution you'd like to use. The example dataset uses the "Systematic Subsample - 7.5 arc-sec" resolution.

3) Download the files and move them into a folder in the project directory (default expected: raster)

4) Suggested citation: Danielson, J.J., and Gesch, D.B., 2011, Global multi-resolution terrain elevation data 2010 (GMTED2010): U.S. Geo- logical Survey Open-File Report 2011–1073, 26 p.


### Shape file for map mask: '--mask country'
To extract the part of the map that is of interest, TopoMap makes use either of a set of coordinates (see below), or a polygon in the shape of the country of interest. 

Natural Earth Data provides one such source of shape files for countries. Different versions of these (varying by how borders are defined) can be downloaded [here](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/)

They can also be downloaded per country from the GADM [here](https://gadm.org/download_country.html), but these files are MUCH larger. 

A custom polygon can also be used using the '--mask country' option. Simply provide a custom shape file. 


### Coordinates for map mask: '--mask coords'



### Sample data
