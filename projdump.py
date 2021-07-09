# Dump PROJ database to PROJ4JS Strings
# Answered by mikewatt on gis.stackexchange
# https://gis.stackexchange.com/questions/403432/how-do-i-dump-proj-epsg-database-to-proj4js-compatible-proj-strings/
# script prepared by Saijin-Naib
import json
import pyproj

crs_list = pyproj.database.query_crs_info()
crs_dict = {}

for info in crs_list:
    crs = pyproj.CRS.from_authority(info.auth_name, info.code)
    crs_dict[f'{info.auth_name}:{info.code}'] = crs.to_proj4()

print(json.dumps(crs_dict))
