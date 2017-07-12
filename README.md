# gthOSM

Steps to generate ground truth image from open street map,

The following tools were used to convert the open street map in pbf format to a tif file. Note there could be other steps to accomplish the following.

1. One band of Sentinel-1 (or other sensor) image in geotiff format is required. The image shown is VH band of S1 image over the region of France.



2. Openstreet map in pbf format could be dowloaded from http://download.geofabrik.de/ for a country or states for large countries.
For France it is named: france-latest.osm.pbf

3. To select just the features in openstreet map for the given area, bounding box for the S1 image needs to be found and stored in a file say france.poly with contents:
france
1
     0.450E+01    0.4705E+02
     0.576E+01    0.4705E+02
     0.576E+01    0.4586E+02
     0.450E+01    0.4586E+02
END
END

4. Next use the tool osmosis to select features in the bounding box (name: france_poly.osm.pbf). 

The command ::

bin/osmosis --read-pbf file="/data/france-latest.osm.pbf" --bounding-polygon file="/data/france.poly" --write-pbf file="/data/france_poly.osm.pbf"

5. A specific feature or class can be extracted by the following python script: 

python [forests.py(https://github.com/sankar19/gthOSM/forests.py)]  /data/france_poly.osm.pbf /data/forests_france.pbf

The python script was extended from pyosmium examples [https://github.com/osmcode/pyosmium/blob/master/examples/filter_coastlines.py].



