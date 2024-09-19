import arcpy
import re

arcpy.env.workspace = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput = True

countries = r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
disputed_areas = r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_disputed_areas.shp"
output_req_6 = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_6'

arcpy.MakeFeatureLayer_management(countries, 'countries_disputed_areas_with_income_lessThan_4')

arcpy.MakeFeatureLayer_management(disputed_areas, "disputed_grp_layer", """ "INCOME_GRP" NOT LIKE '%5%' AND "INCOME_GRP" NOT LIKE '%4%' """)
print("Names of created disputed areas:")
with arcpy.da.SearchCursor("disputed_grp_layer", ["NAME"]) as cursor:
 for row in cursor:
    print(row[0])
    arcpy.FeatureClassToFeatureClass_conversion("disputed_grp_layer", output_req_6, "disputed_grb_l4.shp")
