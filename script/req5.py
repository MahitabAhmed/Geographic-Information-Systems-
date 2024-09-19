import arcpy
import re

arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
urban_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_urban_areas.shp"
output_req_5 = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_5'

arcpy.MakeFeatureLayer_management(urban_areas, 'urban_areas_layer')

countries_cursor = arcpy.SearchCursor(countries,['CONTINENT','SOVEREIGNT'])
for x in countries_cursor:
    if x.getValue('CONTINENT') == 'Asia' or x.getValue('CONTINENT') ==  'Europe' or x.getValue('CONTINENT') == 'North America':
        Sovereignt = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
        arcpy.MakeFeatureLayer_management(countries,'countries_urban_areas', """ "CONTINENT" = '{}' """.format(x.getValue('CONTINENT')))
        arcpy.SelectLayerByLocation_management('urban_areas_layer','WITHIN','countries_urban_areas')
        arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer', output_req_5, 'urban_areas_in_{}'.format(x.getValue('CONTINENT')))
        print('urban_areas_in_{}'.format(x.getValue('CONTINENT')) + '_with_Sovereignt_{}'.format(Sovereignt))
