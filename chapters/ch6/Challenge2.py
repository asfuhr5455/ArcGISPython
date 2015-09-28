import arcpy
from arcpy import env
env.overwriteOuput = True
env.workspace = "P:/Python/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("P:/Python/Python/Data/Exercise06/Results", "Stuff.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == 'Polygon':
        arcpy.CopyFeatures_management(fc, "P:/Python/Python/Data/Exercise06/Results/Stuff.gdb/" + fcdesc.basename)
