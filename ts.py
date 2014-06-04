# Travelling Suitcase
from xml.etree.ElementTree import parse

d_lat = 41.98062
d_lon = -87.668452

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
	if float(bus.findtext('lat')) > d_lat and bus.findtext('d').startswith('North'):
		print(','.join([bus.findtext('id'),bus.findtext('dd'),bus.findtext('lat'),bus.findtext('lon')]))

d=input("Press <enter>")