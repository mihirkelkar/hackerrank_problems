import urllib
from random import choice
def journeys():
	colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#800000', '#008000', '#000080', '#808000', '#008080', '#800080']
	fp = open('journeys', r'U')
	mp = open('coords', 'w')
	temp = fp.readlines()
	final_list = []
	for i in temp:
		cities = i.strip().split(',')
		home = find_lat_long(cities[0])
		dest = find_lat_long(cities[1])
		mp.write(' '.join(home) + '\n')
		mp.write(' '.join(dest) + '\n')
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
	
