import arcpy
import re

arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

airport=arcpy.arcpy.GetParameterAsText(0)

airports_list = arcpy.ListFields(airport)
fields = []

for x in airports_list:
    if x.type == 'String':
        fields.append(x.name)
    else:
        print ("This is not a String, it is a {}".format(x.type))

for airporti in fields:
    with arcpy.da.UpdateCursor(airport, [airporti, 'name_en']) as update_airport:
        for x in update_airport:
            if x[0] == ' ':
                x[0] = x[1]
                update_airport.updateRow(x)
                print("updated")
                arcpy.AddMessage("Success")
