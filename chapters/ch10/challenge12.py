import arcpy
mxd = arcpy.mapping.MapDocument("P:\Python\Python\Data\Exercise10\Austin_TX.mxd)
df = arcpy.mapping.ListDataFrames(mxd, "Facilities")[0]
addLayer = arcpy.mapping.Layer(r"P:\Python\Python\Data\Exercise10\Austin/parks.shp")
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
mxd.saveACopy(r"C:\Project\Project2.mxd")
del mxd, addLayer
