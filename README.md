# gthOSM

Steps to generate ground truth image from open street map,

The following tools were used to convert the open street map in pbf format to a tif file. Note there could be other steps to accomplish the following.


1. One band of Sentinel-1 or 2 (or other sensor) image in geotiff format is required. The RGB image over the region of France is shown below:

Sentinel-2 image courtesy of "Copernicus Sentinel data [2017]"

![alt text](https://github.com/sankar19/gthOSM/blob/master/France1_RGB_rsz.jpg)


2. Openstreet map in pbf format could be dowloaded from http://download.geofabrik.de/ for a country or states for large countries.
For France it is named: france-latest.osm.pbf

3. To select just the features in openstreet map for the given area, bounding box for the S1 image needs to be found and stored in a file say [france.poly](https://github.com/sankar19/gthOSM/france.poly ).


4. Next use the tool osmosis to select features in the bounding box (name: france_poly.osm.pbf). The command ::

    ```bin/osmosis --read-pbf file="/data/france-latest.osm.pbf" --bounding-polygon file="/data/france.poly" --write-pbf file="/data/france_poly.osm.pbf"```


5. A specific feature or class can be extracted by the following python script [forests.py](https://github.com/sankar19/gthOSM/forests.py). The python script was extended from pyosmium [examples](https://github.com/osmcode/pyosmium/blob/master/examples/filter_coastlines.py).

    ```python forests.py /data/france_poly.osm.pbf /data/forests_france.pbf```

6. Then two tools are used to convert the .pbf to .geojson

    ```./osmconvert64 /data/forests_france.pbf > /data/forests_france.osm```

    ```osmtogeojson /data/forests_france.osm > /data/forests_france.geojson```


7. In the final step, binary image for the forest class is obtained by utilizing rio raserize tool.

    ```rio rasterize /data/forests_france.tif --like /data/VH_SAR.tif < /data/forests_france.geojson```


8. Ground truth with three classes are shown below for the France image [forest, farmland and water, river]

![alt text](https://github.com/sankar19/gthOSM/blob/master/France1_gth_rsz.png)



9. If you find the process helpful, you can cite the website. Classification results will be available in the following papers;

S. Piramanayagam, et al. , “Supervised Classification of Multisensor Remote Sensed Images using Deep Learning Framework”, for submitted to ISPRS Journal, 2017.

S. Piramanayagam, et al. , “Classification of remote sensed images using random forests and CRF-RNN framework”, SPIE remote sensing, 2016.


# Pre-requisites

The above process require installation of various tools in the linux machine:

1. rasterio (https://github.com/mapbox/rasterio)
2. osmtogeojson (https://github.com/tyrasd/osmtogeojson)
3. osmconvert64
4. osmosis (http://wiki.openstreetmap.org/wiki/Osmosis/Installation)
