import arcpy
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for features in fc:
    for row in cursor:
        length = length + row[0]
    print length
