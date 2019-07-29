#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

INPATH = "/lidar2019/03_DOM_25cm_TIFF/"
OUTPATH = "/lidar2019/99_Derivate/dom/"
TMPPATH = "/tmp/"

shp = ogr.Open("/lidar2019/99_Derivate/lidar2019.shp")
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    print "**********************: " + infileName

    basename = os.path.splitext(infileName)[0]
    infile = os.path.join(INPATH, infileName)
    outfile = os.path.join(OUTPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -ot Float32 "
    cmd += infile + " " + outfile
    print cmd
    os.system(cmd)
    print "**********************: "

    infile = outfile
    cmd = "gdaladdo -r average " + infile + " 2 4 8 16 32"
    print cmd
    os.system(cmd)
