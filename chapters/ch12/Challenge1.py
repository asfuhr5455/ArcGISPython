import arcpy
arcpy.env.workspace = "P:/Python/Python/Data/Exercise12"


def countstringfields(x):
    b = arcpy.ListFields(x)
    a = 0
    for fields in x:
        if type(fields) == str:
            a = a + 1
    return a
    print a
