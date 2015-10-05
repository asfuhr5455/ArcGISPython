import arcpy
import fileinput
import string
import os
from arcpy import env
coordinates = (0,0), (0, 1000), (1000, 0), (1000, 1000)
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Python/Python/Data/Exercise08"
newfc = "Results/newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = coordinates
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
