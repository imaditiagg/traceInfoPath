
#!/usr/bin/env python
# encoding: utf-8
import tweepy
import json
import pymongo

#Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#refer http://docs.tweepy.org/en/v3.2.0/api.html#API
#tells tweepy.API to automatically wait for rate limits to replenish


def save_to_mongo(data,mongo_db,mongo_db_coll,**mongo_conn_kw):
    client=pymongo.MongoClient(**mongo_conn_kw)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    data["hashtag"]='';
    data["category"]='';
    return coll.insert(data)

users =tweepy.Cursor(api.search,q='').items()
count = 0
errorCount=0
#file = open('search.json', 'w') 

while True:
    try:
        user = next(users)
        count += 1
        #use count-break during dev to avoid twitter restrictions
        #if (count>10):
        #    break
    except tweepy.TweepError:
        #catches TweepError when rate limiting occurs, sleeps, then restarts.
        #nominally 15 minnutes, make a bit longer to avoid attention.
        print "sleeping...."
        time.sleep(60*16)
        user = next(users)
    except StopIteration:
        break
    try:
        print "Writing to JSON tweet number:"+str(count)
        save_to_mongo(user._json,'Twitter','Tweets')
        #print user._json
        #json.dump(user._json,file,sort_keys = True,indent = 4)
        
        
    except UnicodeEncodeError:
        errorCount += 1
        print "UnicodeEncodeError,errorCount ="+str(errorCount)

print "completed, errorCount ="+str(errorCount)+" total tweets="+str(count)
    
   


























