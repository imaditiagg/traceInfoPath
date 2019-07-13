import tweepy
import json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pymongo import MongoClient

MONGO_HOST= 'mongodb://localhost/tweets'  


client = MongoClient(MONGO_HOST)
db = client.tweets         

collection = db['twitterdb']		

#insert keys
# Twitter initialization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetCount = 0
search_phrase = 'comprehensive'

status=[]

# ID of the most recent tweet
max_id = -1

new_statuses = api.search(q=search_phrase, count="10", include_entities= True)  

for item in new_statuses:
	tweetCount += 1
	with open('/home/himshi/Minor/New/tweet'+str(tweetCount)+'.json', 'w') as outfile:
			json.dump(item.text,outfile)
	status.append([item.text.encode('utf-8')])	

for st in status:
	print st


