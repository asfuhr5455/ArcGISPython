import arcpy
from arcpy import env
env.workspace = "P:/Python/Python/Data/Exercise07"
FC = "airports.shp"
rows = arcpy.SearchCursor(FC)
fields = arcpy.ListFields(FC)
for field in fields:
    if field.name == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))

#The if statement is missing a colon.
#fc is lowercase in parentheses.
#The if statement should be field instead of fields.
#line 10 needs an indent with the print statement
        
