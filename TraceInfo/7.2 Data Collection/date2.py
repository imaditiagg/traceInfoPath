import pymongo
import csv

import codecs
from datetime import datetime
import json
#import requests
import os
import string
import sys
import time

row = csv.writer(open("h.csv", "a"))
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.Twitter
data = db.Tweets.find()
count=0
l=[]
for d in data:
    
    if d["hashtag"] == "":
      mytime = d['created_at']
      #datetime =  mytime.date.encode( 'ascii', 'ignore')
      #struct_date = time.strptime(datetime, "%a, %d %b %Y %H:%M:%S +0000")
      c = time.strptime(mytime.replace("+0000",''), '%a %b %d %H:%M:%S %Y')

      secs = time.mktime(c)
      tm = time.asctime(time.localtime(secs))
      
      #date = time.strftime("%b/%d/%Y")
      #tm = time.strftime("%b/%d/%Y %H:%M:%S")
      #tm = time.strftime("%H:%M:%S")

      #print tm
      l.append(tm)

print l[0]
s=len(l)
print l[s-1]
row.writerow(["",l[s-1],l[0]])

