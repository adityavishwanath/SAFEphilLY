#!/usr/bin/env python

from urllib2 import urlopen
import json
from sklearn import cross_validation
from sklearn.svm import SVC
from time import time
import numpy as np

#Inserted the API Key into the base URL. This ugly hack will work for now
BASE_URL = "https://data.phila.gov/resource/sspu-uyfa.json?$$app_token=bF12rIkELtbJ8PXnuzuZTWmVF"

#REPLACE THESE WITH ACTUAL VALUES
longitude = "%20-75.176386"
latitude = "%2039.916687"

radius = "%20500" #set radius to 500 meters

#Find all points around a specified radius
location_url = BASE_URL+ ("&$where=within_circle(shape,%s,%s,%s)" % (latitude, longitude, radius))

response = urlopen(location_url)
data = json.loads(response.read().decode('utf-8'))

num_data_points = len(data)
print "Number of total data points = " + str(num_data_points)

'''

Sample Data Entry in the data list:

{u'text_general_code': u'Other Assaults', u'ucr_general': u'800', u'hour': u'18', 
u'dc_key': u'201501020274', u'psa': u'2', u'dispatch_date': u'2015-05-30', u'location_block': u'1700 BLOCK STOCKER ST', 
u'shape': {u'type': u'Point', u'coordinates': [-75.177232, 39.915826]}, u'dispatch_date_time': u'2015-05-30T18:17:00.000', 
u'dc_dist': u'01', u'dispatch_time': u'18:17:00'}

'''

training_data = []
training_labels = []

for d in data:
	ucr = d.get('ucr_general')
	if ucr != None:
		if not (ucr == 700 or ucr == 1000 or ucr == 1100 or ucr == 1200 or ucr == 1300 or ucr == 1500 or (ucr > 1500 and ucr <= 2400) or ucr == 2600):
			training_data.append((int(d.get('hour'))))
			ucr_general_number = int(d.get('ucr_general'))
			#Round down the UCR Number to the nearest 100
			rounded_ucr_general = ucr_general_number - (ucr_general_number % 100)
			training_labels.append(rounded_ucr_general)

#Need to reshape the training data because the vector is in 1D
all_training_data = np.array(training_data).reshape(-1,1)
all_training_labels = np.array(training_labels)

#Split all the data points into training and testing data
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(all_training_data, all_training_labels, test_size=0.1, random_state=42)

print "Number of training data points = " + str(len(features_train))
print "Number of testing data points = " + str(len(features_test))

#Instantiate the Classifier. We use a support vector machine with an rbf kernel
classifier = SVC(kernel="rbf", C=10000.0)
if classifier == None:
    print "Something went wrong - check packages!"
    print
    exit(1)

#Get first timestamp
time0 = time()

#Fit the data
classifier.fit(features_train, labels_train)

#Get second timestamp
training_time = round(time()-time0, 4)

print "The training time was = " + str(training_time) + " seconds"

#Use the testing data to find the accuracy of the model
accuracy = classifier.score(features_test, labels_test)
print "The Accuracy Score is = " + str(round(accuracy * 100, 3)) + " %"