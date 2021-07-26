# Mini-project II
The details for the miniproject from Week 2


In this miniproject, we will combine and practice topics that we have learned in previous two weeks:
- APIs
- Databases (SQL)
- Pandas
- Processing special data types in Python

We will work with these APIs:
1. [Foursquare](https://developer.foursquare.com/places) - we have already come across this one
2. [Yelp](https://www.yelp.com/developers/documentation/v3/get_started) - this API offers similar services as Foursquare.
3. (Stretch) [Google Places API](https://developers.google.com/places/web-service/intro) - this google api offers similar service as well.

The main goal of the mini-project is to build the database of restaurants, bars and various points of interest (POIs) in the area of your choice and find out which API has better coverage in the selected area. The APIs have limited number of requests for free, so start with the smaller area. The project consists of following tasks:

- pull the data about various POIs in the area through API. (Search Yelp for companiees that are in the area using [these instructions](https://www.yelp.com/developers/documentation/v3/business_search)). If you run out of requests for any of the APIs, don't worry, it's ok to use only sample data you already have or the POIs from the Yelp API. It's approach and process that counts, not the actual number of places we were able to get.
- create own SQLite database and store the data about the POIs. Think about what will be the best structure of the database. We've used and created sqlite3 databases before in the activity [**SQL in Python**](https://data.compass.lighthouselabs.ca/b9e08cd5-68c6-490c-a32b-a66f01bf53e1).
- compare the results using SQL or Pandas (it's up to you:)) and see which API has a better coverage of the area.
- choose the top 10 POIs based on the popularity (number of reviews or average rating) ([Yelp](https://www.yelp.com/developers/documentation/v3/business), [Foursquare](https://developer.foursquare.com/docs/api-reference/venues/details/)).
- (Stretch) By implementing [travelling salesman problem (TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem), how much time would it take to visit all of these places? ([Directions API](https://developers.google.com/maps/documentation/directions/start) from google will be helpful here). We will have to find travel time between all places (top 10). We can use [ortools](https://developers.google.com/optimization/routing/tsp) from Google to effectively implement TSP. These tools are very powerful and [easy to install](https://developers.google.com/optimization/install).

We have a lot of work so let's start right away. Enjoy!!


> #### Note
> Some APIs from Google aren't for free anymore but each account has 200$ credit every month. Therefore we are able to use these services for learning purposes for free.
