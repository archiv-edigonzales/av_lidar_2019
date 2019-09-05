#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

VRT = "/Samsung_T5/ch.so.agi.lidar_2019.dtm/dtm_no_alpha.vrt"
OUTPATH = "/Samsung_T5/99_Derivate/contours/"
TMPPATH = "/tmp/"
BUFFER = 50

shp = ogr.Open("/vagrant/lidar2019.shp")
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    basename = os.path.splitext(infileName)[0]
    print "**********************: " + infileName

    if os.path.exists(os.path.join(OUTPATH, basename + "_50cm.zip")):
        continue
        
    geom = feature.GetGeometryRef()
    env = geom.GetEnvelope()

    minX = int(env[0] + 0.001)
    minY = int(env[2] + 0.001)
    maxX = int(env[1] + 0.001)
    maxY = int(env[3] + 0.001)
    

    outfile = os.path.join(TMPPATH, "input.tif")
    
    cmd = "gdalwarp -overwrite -s_srs epsg:2056 -t_srs epsg:2056 -te" 
    cmd += " " + str(minX - BUFFER) + " " +  str(minY - BUFFER) + " " +  str(maxX + BUFFER) + " " +  str(maxY + BUFFER)
    cmd += " -tr 0.25 0.25 -wo NUM_THREADS=ALL_CPUS -r bilinear "
    cmd += " " + VRT + " " + outfile
    print cmd    
    #os.system(cmd)

    infile = os.path.join(TMPPATH, "input.tif")
    outfile = os.path.join(TMPPATH, "output.tif")
        
    for i in range(10):
        cmd = "gdalwarp -overwrite -s_srs epsg:2056 -t_srs epsg:2056"
        cmd += " -r cubicspline " + infile + " " + outfile
        #os.system(cmd)
        #os.system("cp " + outfile + " " + infile)

    infile = os.path.join(TMPPATH, "input.tif")
    outfile = os.path.join(TMPPATH, "contour_tmp_1.shp")
    cmd = "gdal_contour -b 1 -3d -a elev -i 0.5 " + infile + " " + outfile
    print cmd
    #os.system(cmd)
    #os.system("rm " + infile)

    clip = geom.ExportToWkt()
    
    infile = os.path.join(TMPPATH, "contour_tmp_1.shp")
    outfile = os.path.join(OUTPATH, basename + "_50cm.shp")

    cmd = "ogr2ogr -clipsrc '" + clip + "' " + outfile + " " + infile
    print cmd
    #os.system(cmd)

    cmd = "cd " + OUTPATH
    #os.system(cmd)
    cmd = "cd " + OUTPATH + " && zip -D " + os.path.join(OUTPATH, basename + "_50cm.zip") + " " + os.path.join(basename + "_50cm.*")
    print cmd    
    #os.system(cmd)

    os.system("rm " + os.path.join(OUTPATH, basename + "_50cm.dbf"))
    os.system("rm " + os.path.join(OUTPATH, basename + "_50cm.prj"))
    os.system("rm " + os.path.join(OUTPATH, basename + "_50cm.shp"))
    os.system("rm " + os.path.join(OUTPATH, basename + "_50cm.shx"))

    break