import json
from urllib2 import urlopen
from main import ml_code

#GET INPUT HERE IN THE FORM OF "wharton business school", and convert it into "wharton+business+school"
origin_val = "wharton+philadelphia" #temp dummy value
destination_val = "philadelphia+museum+of+art" #temp dummy value

maps_url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%st&key=AIzaSyDXP921qJVZ0kwzYmTp17pSWKJyC4v7clU&mode=walking&alternatives=true" % (origin_val,destination_val)

response = urlopen(maps_url)
data = json.loads(response.read().decode('utf-8'))

coordinate_list = []
number_routes = len(data.get('routes'))
x = 0
for route in data.get('routes'):
	coordinate_list.append([])
	for step in (route.get('legs')[0].get('steps')):
		lat = step.get('start_location').get('lat')
		lon = step.get('start_location').get('lng')
		coordinate_list[x].append((lat,lon))
	x+=1

import datetime
now = datetime.datetime.now()

weighted_values_list = []
x = 0
for route in coordinate_list:
	weighted_values_list.append([])
	y = 0
	for step in route:
		weighted_values_list[x].append(ml_code(str(coordinate_list[x][y][0]), str(coordinate_list[x][y][1]), now.hour))
		y+=1
	x+=1

x = 0
minimum = float(999999999)
second_minimum = minimum
min_route = 0
for route in weighted_values_list:
	if minimum > (float(sum(route))/len(route)):
		second_minimum = minimum
		minimum = sum(route)/len(route)
		min_route = x
	x+=1

if second_minimum == float(999999999):
	second_minimum = float(sum(weighted_values_list[2]))/len(weighted_values_list[2])

print
print "*************************"
print "The best route to take at " + "%s:%s:%s" % (str(now.hour), str(now.minute), str(now.second)) + " is:"
print coordinate_list[min_route]
print "This route is " + str(((second_minimum - minimum) / float(second_minimum))*100) + " % " + "safer than the next safest route!"
print "Thank goodness for ML!"
print "*************************"