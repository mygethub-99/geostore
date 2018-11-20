# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:48:49 2018
https://geohackweek.github.io/vector/04-geopandas-intro/
@author: ow4253
"""
from __future__ import (absolute_import, division, print_function)
from os import path

import matplotlib as mpl
import matplotlib.pyplot as plt

from shapely.geometry import Point
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from shapely.wkt import loads
data_path = r"C:\Users\ow4253\Documents\FMEData\spatial\shapefileplay"

GeoSeries([loads('POINT(1 2)'), loads('POINT(1.5 2.5)'), loads('POINT(2 3)')])
gs = GeoSeries([Point(-120, 45), Point(-121.2, 46), Point(-122.9, 47.5)])
gs.crs = {'init': 'epsg:4326'}
gs.plot(marker='*', color='red', markersize=100, figsize=(4, 4))
plt.xlim([-123, -119.8])
plt.ylim([44.8, 47.7]);

data = {'name': ['a', 'b', 'c'],
        'lat': [45, 46, 47.5],
        'lon': [-120, -121.2, -122.9]}

geometry = [Point(xy) for xy in zip(data['lon'], data['lat'])]
gs = GeoSeries(geometry, index=data['name'])
df = pd.DataFrame(data)
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
gdf = GeoDataFrame(df, geometry=geometry)
gdf.plot(marker='*', color='green', markersize=100, figsize=(5, 5));
sites = gpd.read_file(path.join(data_path,"nsbbuf.shp"))
sites.crs
sites.plot(cmap="Set1", figsize=(10,10))
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.head(2)
world.crs
world.plot(ax=sites.plot(cmap='Set2', figsize=(10, 10)), facecolor='gray');
