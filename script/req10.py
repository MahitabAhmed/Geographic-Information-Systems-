import arcpy
import re


arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

countries = arcpy.GetParameterAsText(0)
urbanareas = arcpy.GetParameterAsText(1)
output_req_10 = arcpy.GetParameterAsText(2)

area_sqkm = float(arcpy.GetParameterAsText(3))

arcpy.MakeFeatureLayer_management(urbanareas, 'urban_areas_layer', """ "area_sqkm" > {} """.format(area_sqkm))

countriesCursor = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'REGION_UN'])
for x in countriesCursor:
    name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "REGION_UN" = 'Africa' AND "FID"= {} """.format(x.getValue('FID')))
    arcpy.SelectLayerByLocation_management('urban_areas_layer', 'WITHIN', 'countries_layer')
    selected_count = int(arcpy.GetCount_management('urban_areas_layer').getOutput(0))
    if selected_count > 0:
        arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer', output_req_9, 'UrbanAreas_in{}_{}'.format(name, x.getValue('FID')))
    arcpy.AddMessage("Success")






