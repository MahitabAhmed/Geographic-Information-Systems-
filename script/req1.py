import arcpy
import re


arcpy.env.workspace=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data'
arcpy.env.overwriteOutput= True

point=r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_populated_places.shp'
countries=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_countries.shp"
disputed_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_admin_0_disputed_areas.shp"
airport=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_airports.shp"
urban_areas=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\data\ne_10m_urban_areas.shp"
output=r"D:\fourth-year\Second-Term\Geographic-Information-Systems\project\output"


list_feature=arcpy.ListFeatureClasses()
print (list_feature)



