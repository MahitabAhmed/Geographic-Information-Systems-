import arcpy

arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

point=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_populated_places.shp'
countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
disputed_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_disputed_areas.shp"
output_req_2 = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_2'

arcpy.MakeFeatureLayer_management(point, 'points_layer')
arcpy.MakeFeatureLayer_management(disputed_areas, 'disputed_areas_layer')
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME"='Palestine' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
arcpy.SelectLayerByLocation_management('disputed_areas_layer', 'WITHIN', 'countries_layer')

arcpy.FeatureClassToFeatureClass_conversion('points_layer', output_req_2, 'cities_in_Palestine')
arcpy.FeatureClassToFeatureClass_conversion('disputed_areas_layer', output_req_2, 'disputed_areas_in_Palestine')

cities_in_Palestine=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_2\cities_in_Palestine.shp'
disputed_areas_in_Palestine=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_2\disputed_areas_in_Palestine.shp'

citis_in_palastineCursor = arcpy.SearchCursor(cities_in_Palestine,['NAME'])
print ("cities_in_Palestine: ")
for x in citis_in_palastineCursor:
     print (x.getValue('NAME'))

disputed_areasCursor = arcpy.SearchCursor(disputed_areas_in_Palestine,['NAME'])
print("disputed_areas_in_Palestine: ")
for x in disputed_areasCursor:
     print (x.getValue('NAME'))


# point 3
print ("SOVEREIGNT in disputed_areas_in_Palestine: ")
with arcpy.da.UpdateCursor(disputed_areas_in_Palestine,['SOVEREIGNT'])as disputed_areascursorupdate:
    for x in disputed_areascursorupdate:
        x[0] = 'Palestine'
        disputed_areascursorupdate.updateRow(x)
        print (x[0])

print ("SOV0Name in cities_in_Palestine: ")
with arcpy.da.UpdateCursor(cities_in_Palestine, ['SOV0NAME']) as cities_cursorupdate:
    for x in cities_cursorupdate:
        x[0] = 'Palestine'
        cities_cursorupdate.updateRow(x)
        print (x[0])
