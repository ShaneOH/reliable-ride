#parse geonames US data dump from http://www.geonames.org/export/
#get all places with a population fewer than 50,000
#exclude duplicate places within 5 miles of each other

import csv
import os
from math import radians, cos, sin, asin, sqrt

def main():
	rawData = os.path.join(os.path.dirname(__file__), '../data/US.txt')
	cleanData = os.path.join(os.path.dirname(__file__), '../data/places.csv')
	prevLat = prevLng = 0

	w = csv.writer(open(cleanData, 'wb'), delimiter = ',')
	with open(rawData) as tsv:
		for place in csv.reader(tsv, delimiter = '\t', quoting=csv.QUOTE_NONE):
			if(int(place[14]) > 0 and int(place[14]) < 50000 
			and getDistance(prevLng, prevLat, float(place[5]), float(place[4])) >= 5):
					     #city	state	   lat       long    population
				w.writerow([place[1], place[10], place[4], place[5], place[14]])
				prevLat = float(place[4])
				prevLng = float(place[5])


def getDistance(prevLng, prevLat, currLng, currLat):
	"""
	Calculate great circle distance between
	two given points using the Haversine formula
	"""

	prevLng, prevLat, currLng, currLat = map(radians, [prevLng, prevLat, currLng, currLat])

	lngDiff = currLng - prevLng
	latDiff = currLat - prevLat
	a = sin(latDiff/2)**2 + cos(prevLat) * cos(currLat) * sin(lngDiff/2)**2
	c = 2 * asin(sqrt(a))
	r = 3956
	return c * r

if __name__ == '__main__':
	main()
