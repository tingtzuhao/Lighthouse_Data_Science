<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import twitter
# ADD OTHER PACKAGES WE WILL NEED
import requests as re
from config import *
import json

consumer_key = cons_key
consumer_secret = cons_secr
access_token = acc_token
access_token_secret = acc_secr

api = twitter.Api(
consumer_key = consumer_key,
consumer_secret = consumer_secret,
access_token_key = access_token,
access_token_secret = access_token_secret)

## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
def main(FILTER=[], LANGUAGES=['en'], PATH='output.txt'):
=======
def main(FILTER, LANGUAGES, PATH):
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
=======
def main(FILTER, LANGUAGES, PATH):
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
=======
def main(FILTER, LANGUAGES, PATH):
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
    with open(PATH, 'a') as f:
        
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 
main([':)', ':('], LANGUAGES=['en'])
=======

main(FILTER, LANGUAGES, PATH)
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
=======

main(FILTER, LANGUAGES, PATH)
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
=======

main(FILTER, LANGUAGES, PATH)
>>>>>>> 217dce0bf5a37b2dc12beba9a72847278135c61e
