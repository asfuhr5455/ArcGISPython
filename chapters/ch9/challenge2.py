import arcpy
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise09"
from arcpy.sa import *
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    x = []
    x.append(raster)
    print x
x.save("P:/Python/Python/Data/Exercise09")
    
    
