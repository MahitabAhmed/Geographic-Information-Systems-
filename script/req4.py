import arcpy
import re

arcpy.env.workspace = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput = True

countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
airports = r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_airports.shp"
output_req_4 = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_4'

arcpy.MakeFeatureLayer_management(countries, 'all_countries')
arcpy.MakeFeatureLayer_management(airports, 'military_airports', """ "type" LIKE '%military%' """)

arcpy.SelectLayerByLocation_management('military_airports', 'WITHIN', 'all_countries')
arcpy.FeatureClassToFeatureClass_conversion('military_airports',output_req_4,'military_airports_count')
cursor = arcpy.SearchCursor(countries, ['NAME'])
for row in cursor:
    name = re.sub(r'[^a-zA-Z0-9\s]', '', row.getValue('NAME'))
    arcpy.MakeFeatureLayer_management(countries, 'selected_country', """ "NAME" = '{}' """.format(name))
    arcpy.SelectLayerByLocation_management('military_airports', 'WITHIN', 'selected_country')
    selected_count = int(arcpy.GetCount_management('military_airports').getOutput(0))
    if selected_count > 0:
        arcpy.FeatureClassToFeatureClass_conversion('selected_country', output_req_4, 'country_with_military_airports_{}'.format(name))
        print(name)