import urllib
from random import choice
def journeys():
	colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#800000', '#008000', '#000080', '#808000', '#008080', '#800080']
	fp = open('journeys', r'U')
	mp = open('polylineJS.js', 'w')
	temp = fp.readlines()
	final_list = []
	for i in temp:
		cities = i.strip().split(',')
		home = find_lat_long(cities[0])
		dest = find_lat_long(cities[1])
		print home
		print dest
		color = choice(colors)
		latlng = []
		latlng.append('new google.maps.Latlng(%s, %s)' % (home[0], home[1]))
		latlng.append('new google.maps.Latlng(%s, %s)' %(dest[0], dest[1]))
		latlng = ','.join(latlng)
		jscript = """var routePath = new google.maps.Polyline({
		path: [%s],
		strokeColor: '%s',
		strokeOpacity: 1.0,
		strokeWeight: 2
		});
		routePath.setMap(map);"""%(latlng, color)
		mp.write(jscript)	
	mp.close()

def find_lat_long(addr):
	url = "http://maps.google.com/maps?q=" + urllib.quote(addr) + '&output=js'
	xml = urllib.urlopen(url).read()
	temp = xml[xml.find('{center') + 9: xml.find('}', xml.find('{center'))]
	temp = temp.split(',')
	#print temp
	temp[0] = temp[0][4:]
	temp[1] = temp[1][4:]
	return temp
def main():
	journeys()
main()	
	
