# GeoPlot
Plot samples on a geographic relief map


# Topographic data
GeoPlot requires elevation data in raster format for the area to be plotted. We use the Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010) that contains elevation data for the globe collected from various sources at 7.5 arc-seconds resolution. More information on the dataset can be found [here](https://topotools.cr.usgs.gov/GMTED_viewer/gmted2010_fgdc_metadata.html)

The required grid square(s) can be downloaded from the USGS following [this link](https://topotools.cr.usgs.gov/gmted_viewer/viewer.htm). 

1) Select the grid square(s) you're interested in.

2) Click on the folder for the grid square and select the resolution you'd like to use. The example dataset uses the "Systematic Subsample - 7.5 arc-sec" resolution.

3) Suggested citation: Danielson, J.J., and Gesch, D.B., 2011, Global multi-resolution terrain elevation data 2010 (GMTED2010): U.S. Geo- logical Survey Open-File Report 2011–1073, 26 p.

**path_to_raster default is data/