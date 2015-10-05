import arcpy
from arcpy import env
env.workspace = "P:/Python/ArcGISPython/chapters/ch7"
fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("Results/buffer.shp")
if fieldname == "FEATURES":
    arcpy.Buffer_analysis(fc, unique_name, "15000 METERS")
elif:
    arcpy.Buffer_analysis(fc, unique_name, "75000 METERS")
