import json
import pymongo
import csv

row = csv.writer(open(".csv", "w"))
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.Twitter
data = db.Tweets.find()
count=0
l=[]
for d in data:
    
    if d["hashtag"] == "":
        ids = d["user"]["id"]
        l.append(ids)
       

li=[]
for x in l:
    count=0
    dic={}
    if not li:
        for y in l:
               if x==y:
                   count=count+1
        dic["user_id"] = x
        dic["count"] = count
        li.append(dic)      
    else:
        flag=0
        for item in li:
            if x == item["user_id"]:
               flag=1
               
        if flag ==0:   
            for y in l:
                if x==y:
                   count=count+1
            dic["user_id"] = x
            dic["count"] = count
            li.append(dic)

    #print li
print li
row.writerow(["Hashtag","User_ID", "Count"])
for i in li:
    row.writerow(["", i["user_id"],i["count"]])
   
