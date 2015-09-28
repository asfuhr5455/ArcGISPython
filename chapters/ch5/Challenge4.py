Challenge 4
total = ""
if arcpy.CheckExtension("spatial") == "Available":
    total = total + "spatial"
if arcpy.CheckExtension("3D_Analyst") == "Available":
    total = total + "3D_Analyst"
if arcpy.CheckExtension("network") == "Available":
    total = total + "network"
print "The following extenions are available" + total
