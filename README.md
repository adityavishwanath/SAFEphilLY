## In a nutshell...
This web app allows a user to enter her/his trip's origin and destination and instantly receive a recommendation for the safest route to take. This decision for the 'safest' route is based on historical crime statistics of all the neighborhoods in Philadelphia.

## Inspiration
Many people walk around the city - back home from parties and dinners at night, to parks, coffee shops, and grocery stores during different times of the day, and they also walk to and back from school and work. Like any big city, Philly has its safe and unsafe spots, and people often do not know if a specific neighborhood is safe to pass by during a certain time of the day. We wanted to address this challenge and designed a lightweight web application that makes the 'best-route' decision for you so that you can reach home SAFEphilLY.

## How we built it
We used the [Crime Incidents](https://www.opendataphilly.org/dataset/crime-incidents) Open Dataset for the city of Philadelphia and ran a [support vector machine](http://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) classifier (with an RBF kernel) to perform supervised learning on the crime statistics. Based on our learning algorithm (which we implement in Python using the [scikit-learn](http://scikit-learn.org/stable/) toolkit), we came up with a confidence parameter for the safety of a specific neighborhood at a specific hour of the day.

Next, we implement the same learning algorithm for any route and give it a risk level based on previous crime statistics for the regions it goes through. To provide the user the 'safest path', we do this for multiple routes from the origin to the destination given by the user. We pull this set of routes from the Google Maps API and use a few statistic measures to come up with the 'safest' route from this set. Finally, we plot this route on the map for the user to see.

The front-end is built with [Polymer](https://www.polymer-project.org/1.0/), a lightweight framework that can work even on low-internet speeds. All the ML and statistics work is done on the remote server and we ensure our front-end is as lightweight as possible.

## Challenges we ran into
While Polymer was easy to work with and get started, we had some trouble working with Google Polymer due to its limited functionality as some of the Google Maps functions we needed to use were not available or difficult to use in the elements in Polymer. We also struggled with building a stable and user-friendly web app due to time constraints.

## Accomplishments that we're proud of
We were able to have our frontend and backend components working in tandem. We are proud of our current implementation of the app which suggests the safest route based on crime statistics and time of the day. We also induced a bias in the ML algorithm towards more 'dangerous' crimes - i.e. we trained our algorithm to favor homicide and personal assaults over thefts and minor crimes. This improved the accuracy and authenticity of our results. We studied the dataset _very_ closely to understand trends and the nuances that we needed to account for in our algorithm.

## What we learned
We learned to use machine learning algorithms on publicly available data to draw new associations that could be valuable to the public. We also learned to use google polymer to make elegant and lightweight apps quickly.

## What's next for SAFEphilLY
We would like to improve the user experience with SAFEphilLY and also port it to Android and iOS platforms. We would also like to explore the potential of integrating with cab services such as Uber and Lyft based on the time of the day and the past history of crime in the area.
