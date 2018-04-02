#!/usr/bin/env python2
# -*-coding:UTF-8 -*

import re

'''from mordecai import Geoparser
geo = Geoparser()
message = geo.geoparse("I traveled from Oxford to Ottawa.")'''

# regex to find latitude and longitude
reg_lat = re.compile(r'(\'lat\': \'([-\d.]+)\',)')
reg_lon = re.compile(r'(\'lon\': \'([-\d.]+)\',)')

t0='\'lat\': \'51.75222\','
t1='\'lon\': \'-1.25596\','
message = t0 + t1 + t0 + t1

lat0 = set(reg_lat.findall(message))
lon1 = set(reg_lon.findall(message))

lat = reg_lat.search(message).group(2)
lon = reg_lon.search(message).group(2)

print('{} contain latitude'.format(lat0))

print('latitude: {}'.format(lat))
print('longitude: {}'.format(lon))
