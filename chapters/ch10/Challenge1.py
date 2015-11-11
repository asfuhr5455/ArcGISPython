import arcpy
mxd = "P:/Python/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
print mapdoc
dataframe = arcpy.mapping.ListDataFrames(mapdoc, "Facilities")[0]
layer = "P:\Python\Python\Data\Exercise10\Austin\parks.shp"
addlayer = arcpy.mapping.Layer(layer)
print addlayer
for df in arcpy.mapping.ListDataFrames(mapdoc):
    if df == "Facilities" or df == "Street Trees":
        arcpy.mapping.AddLayer(df, addlayer)
mapdoc.save()
del mxd, addlayer
