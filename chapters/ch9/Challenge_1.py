import arcpy
from arcpy import env
from arcpy.sa import *
elevraster = arcpy.Raster("P:/Python/Python/Data/Exercise09/Elevation")
env.workspace = "P:/Python/Python/Data/Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
# get slope
slope = Slope(elevraster)
# reclassify slope
remap = RemapRange([[0,5,0], [5, 20, 1], [20, 1000, 7]])
outreclass = Reclassify("elevation", "VALUE", remap)
# get aspect
outraster2 = Aspect("elevation")
# reclassify aspect
outreclass2 = RemapRange([[0, 150, 0], [150, 270, 1], [270, 300, 2]])
outreclass = Reclassify("elevation", "VALUE", outreclass2)
# get landcover
a = "landcover.tif"
# relcassify landcover
outreclass3 = RemapRange([[0,41,0], [41,43,1], [43,90,2]])
c = Reclassify("landcover.tif", "VALUE", outreclass3, "NODATA")
# combine all three with map algebra
