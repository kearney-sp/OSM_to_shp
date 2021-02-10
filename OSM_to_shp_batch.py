import osmnx as ox
import os

inDIR = '/Users/spk/Documents/GitHub/OSM_to_shp/osm_dir/'
outDIR = '/Users/spk/Documents/GitHub/OSM_to_shp/shp_dir/'
if not os.path.exists(outDIR):
    os.mkdir(outDIR)

osm_geom = ox.geometries_from_xml(inDIR + 'sol-mountain_trails_trailforks.osm')
osm_geom.drop(columns=['nodes']).to_file(outDIR + 'sol-mountain_trails_trailforks')

