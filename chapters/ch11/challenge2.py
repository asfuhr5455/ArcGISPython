import arcpy
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + " " + str(x) + " by " + str(y) + " " + units + "."

#The line 3 has a forward slash and backward slash.
#In line 5, arcpy.describe should be arcpy.Describe
#In line 4 Landcover.tiff would work if it had one t in tif
#In line 10 there could be a space before str(x)
