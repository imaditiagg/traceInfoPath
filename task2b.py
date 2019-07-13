import tweepy
import json
from pymongo import MongoClient

MONGO_HOST= 'mongodb://localhost/twitterdb'  

#WORDS = ['wonderful']

#insert keys

class Listener(tweepy.StreamListener):    

    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        try:
            client = MongoClient(MONGO_HOST)
            db = client.twitterdb
    
            datajson = json.loads(data)
            
            created = datajson['created_at']

            print("Tweet collected at " + str(created))
           
            db.search.insert(datajson)
        except Exception as e:
           print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


listener = Listener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
#print("Tracking: " + str(WORDS))
print("Tracking: " + str('wonderful'))

streamer.filter(track='wonderful')
#streamer.filter(track=WORDS)
