# monitor.py

import urllib
from xml.etree.ElementTree import parse

candidates = [4164,4354,4353,4159] 	
dl = 41.98062

def distance(lat1,lat2):
	'Return distance between two lats'
	return 69*abs(lat1-lat2)

def monitor():
	u = urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
	doc = parse(u)

	for bus in doc.findall('bus'):
		busid = bus.findtext('id')
		#print("Checking bus id %r" % busid)
		if int(busid) == 4159:
			lat = float(bus.findtext('lat'))
			lon = float(bus.findtext('lon'))
			dis = distance(lat,dl)
			print(busid,dis)
			if dis < 10:
				import webbrowser
				webbrowser.open("http://maps.googleapis.com/maps/api/staticmap?size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C"+str(lat)+","+str(lon)+"&sensor=false")

import time

while True:
	monitor()
	time.sleep(10)
