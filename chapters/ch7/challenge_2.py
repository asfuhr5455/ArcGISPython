import arcpy
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise07"
fc = "Results/airports.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)
fieldlist = arcpy.ListFields(fc)
fieldnames = []
for field in FEATURE:
    if FEATURE == airport:
        fieldnames.append("NO")
    else:
        fieldnames.append("YES")
