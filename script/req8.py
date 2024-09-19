import arcpy
import re


arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

point=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_populated_places.shp'
countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
output_req_8=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output\req_no_8'

arcpy.MakeFeatureLayer_management(point,'cities_in_arabic_countries')
arcpy.MakeFeatureLayer_management(countries,'arabic_countries',""" "REGION_WB" = 'Middle East & North Africa' """)

arcpy.SelectLayerByLocation_management('cities_in_arabic_countries','WITHIN','arabic_countries')

arcpy.FeatureClassToFeatureClass_conversion('cities_in_arabic_countries', output_req_8,'Cities_in_Arabic_countries')
