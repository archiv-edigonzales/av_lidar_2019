#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

#VRT = "/lidar2018/99_Derivate/dtm_25cm/dtm_25cm.vrt"
TINDEX = "/vagrant/lidar2019.shp"
INPATH = "/lidar2019/01_Punktwolke_LAS/"
OUTPATH = "/Samsung_T5/99_Derivate/vegetation/"

shp = ogr.Open(TINDEX)
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    basename = os.path.splitext(infileName)[0]
    print "**********************: " + infileName

    geom = feature.GetGeometryRef()
    env = geom.GetEnvelope()

    minX = int(env[0] + 0.001)
    minY = int(env[2] + 0.001)
    maxX = int(env[1] + 0.001)
    maxY = int(env[3] + 0.001)
    
    bounds = "(["+str(minX)+","+str(maxX-0.25)+"],["+str(minY)+","+str(maxY-0.25)+"])"

    cmd = 'docker run -v /vagrant/scripts:/data -v /lidar2019/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/'+basename+'.las" --writers.gdal.filename="/output/'+basename+'_vegetation.tif" --writers.gdal.bounds="'+bounds+'" --filters.range.limits="Classification[4:5]" /data/rasterize_vegetation.json'
    print cmd
    x = os.system(cmd)

    cmd = "gdaladdo -r average "
    cmd += OUTPATH + basename + "_vegetation.tif" + " 2 4 8 16 32 "
    print cmd
    os.system(cmd)

    #break

