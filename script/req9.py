import arcpy
import re

arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
urban_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_urban_areas.shp"
output_req_9 = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_9'

arcpy.MakeFeatureLayer_management(urban_areas, 'urban_areas_layer', """ "area_sqkm" > 50 """)

countriesCursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'REGION_UN'])
for x in countriesCursor:
    name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "REGION_UN" = 'Africa' AND "FID"= {} """.format(x.getValue('FID')))
    arcpy.SelectLayerByLocation_management('urban_areas_layer', 'WITHIN', 'countries_layer')
    selected_count = int(arcpy.GetCount_management('urban_areas_layer').getOutput(0))
    if selected_count > 0:
        arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer', output_req_9,'UrbanAreas_in{}_{}'.format(name, x.getValue('FID')))
        print(x.getValue('NAME'))
    print("Success")
