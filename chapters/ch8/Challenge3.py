import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Python/Python/Data/Exercise08"
newfc = "Results/newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "C:/Python/Python/Data/Exercise08/Hawaii.shp"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
    cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
