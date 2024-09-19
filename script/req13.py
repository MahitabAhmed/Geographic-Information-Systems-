import arcpy
import re


arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

# disputed_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_disputed_areas.shp"
#
# count = 0
# total_count = 0
#
# with arcpy.da.UpdateCursor(disputed_areas,['POP_YEAR','ECONOMY','NAME']) as update_economy:
#     for x in update_economy:
#         total_count += 1
#         if x[0] < 2014:
#             x[1] = 'updated!'
#             update_economy.updateRow(x)
#             count += 1
#             print("updated disputed area: "+ x[2])
#
# print("updated: ")
# print (count)
# print("total_count: ")
# print (total_count)

disputed_areas = arcpy.arcpy.GetParameterAsText(0)
pop_year = arcpy.arcpy.GetParameterAsText(1)

count = 0
total_count = 0

with arcpy.da.UpdateCursor(disputed_areas, ['POP_YEAR', 'ECONOMY', 'NAME']) as update_economy:
    for x in update_economy:
        total_count += 1
        if x[0] < int(pop_year):
            x[1] = 'updated!'
            update_economy.updateRow(x)
            arcpy.AddMessage("Success")
            arcpy.AddMessage("updated disputed area: " + x[2])
            count += 1
            print("updated disputed area: " + x[2])

arcpy.AddMessage(count)
print("updated: ")
print (count)

arcpy.AddMessage(total_count)
print("total_count: ")
print (total_count)
