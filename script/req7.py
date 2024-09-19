import arcpy

arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
airport=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_airports.shp"
output_req_7=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_7'

arcpy.MakeFeatureLayer_management(countries,'countries_ramp_airports')

airport_Cusor=arcpy.SearchCursor(airport,['name','location','wikipedia'])
for x in airport_Cusor:
    arcpy.MakeFeatureLayer_management(airport,'airport_Layer',""" "location" = 'ramp' """)
    arcpy.SelectLayerByLocation_management('airport_Layer','WITHIN','countries_ramp_airports')
    arcpy.FeatureClassToFeatureClass_conversion('airport_Layer',output_req_7,'countries_with_ramp_airports')

count = 0
countries_ramp_airports=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\output_req_7\countries_with_ramp_airports.shp'
ramp_airport_Cusor=arcpy.SearchCursor(countries_ramp_airports,['name','location','wikipedia'])
for x in ramp_airport_Cusor:
    print (x.getValue('name'))
    print (x.getValue('location'))
    print (x.getValue('wikipedia'))
    count += 1
print count
