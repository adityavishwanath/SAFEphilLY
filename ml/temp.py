import json
from urllib2 import urlopen



url = "https://maps.googleapis.com/maps/api/directions/json?origin=wharton+philadelphia&destination=philadelphia+museum+of+art&key=AIzaSyDXP921qJVZ0kwzYmTp17pSWKJyC4v7clU&mode=walking&alternatives=true"

response = urlopen(url)
data = json.loads(response.read().decode('utf-8'))

print len(data.get('routes'))

print data.get('routes')[0]

print "********************************"
print "********************************"

print data.get('routes')[1]

print "********************************"
print "********************************"

print data.get('routes')[2]