import json
import pymongo
import csv

#row = csv.writer(open("h.csv", "w"))
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.Twitter
data = db.Tweets.find()
count=0
l=[]
for d in data:
    
    if d["hashtag"] == "CBSEPaperLeak":
        count=count+1

print count

