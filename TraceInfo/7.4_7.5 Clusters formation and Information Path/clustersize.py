import pymongo
import csv
import tweepy
import networkx as nx


row = csv.writer(open("cluster_info.csv", "a"))
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.Twitter
data = db.Tweets.find()
count3=0
l=[] #list of dictionaries
for d in data:
    dict1={}
    if d["hashtag"] == "#SackMamataGovt":
              dict1["id"]=d["id"]
              dict1["text"] = d["text"]
              dict1["user"] =d["user"]["screen_name"]
              if "retweeted_status" in d:
                  dict1["origin_id"]= d["retweeted_status"]["id"]
              dict1["is_quote_status"]=d["is_quote_status"]
              if "quoted_status_id" in d: 
                   dict1["quoted_status_id"] = d["quoted_status_id"]
                  
              if "quoted_status" in d:
                  if "quoted_status_id" in d["quoted_status"]:
                      dict1["quote_of_quoted_id"]= d["quoted_status"]["quoted_status_id"]
                      #print dict1["text"] #check if quote of quoted tweets are present
                      #print "\n"
                      
              l.append(dict1)

print "\nTotal tweets"
print len(l) #total tweets
"""
for ele1 in l:
    if "quote_of_quoted_id" in ele1:
        var = ele1["quote_of_quoted_id"]
        for ele2 in l:
            if "quote_of_quoted_id" in ele2 and var == ele2["id"]:
               print "matched"

"""



newli=[] #list of lists

for x in l:
    
 if ("origin_id" in x) and (not (x["is_quote_status"])):
    li=[] 
    li.append(x["id"])
    #print "x added "
    #print x["text"]
    #print "\n"
    for y in l:
      if ("origin_id" in y) and  (not (y["is_quote_status"])):
       if x["text"] == y["text"] and x!=y:
                 #means it is retweeted tweet
                 #append tweet id in list
         li.append(y["id"])
         #print "y added"
         #print y["text"]
         #print "\n"
                  
         s = y["origin_id"]   
             
    if len(li)> 1:           
    
         for item in l:
          if s == item["id"]:  #include origin
           li.append(item["id"])
           #print "origin added "
           #print item["text"]
           #print "\n"
           for item2 in l:
             if "quoted_status_id" in item2:
               if s == item2["quoted_status_id"]: #include quoted tweets and retweet of quoted tweets
                  li.append(item2["id"])
                  #print "quoted tweet added "
                  #print item2["text"]
                  #print "\n"
                  for item3 in l:
                    if "quote_of_quoted_id" in item3:
                      if s == item3["quote_of_quoted_id"]: #include quoted of quoted tweets
                          li.append(item3["id"])
                          #print "quote of quoted tweet added "
                          #print item3["text"]
                          #print "\n"


         
     #len(li)=1 means no exact match found for the tweet  
         newli.append(li); #append that list of similar tweet id's in newlist
    else :
         count3=count3+1
    


 #print "one pass done"
 #break
 
 
print "\nclusters of length 1 which were excluded"
print count3

print "\nTotal No of clusters(containing duplicates)"
print len(newli) #print total no. of clusters formed of similar tweets

count=0
for x in newli:
    for y in x:
        count =count +1

print "No of tweets covered"
print count #no. of tweets covered in exact match


for item in newli:
 item.sort()

newli.sort()

i = len(newli) - 1
while i > 0:  
    if newli[i] == newli[i - 1]:
     newli.pop(i)
    i -= 1

#print newli
print "After removing duplicate clusters"
print len(newli)
cluster_size=[]

for x in newli:
    count2=0
    for y in x:
        count2 =count2 +1
    cluster_size.append(count2)

#write in csv hashtag,no. of clusters, size of each cluster
row.writerow(["#SackMamataGovt",len(newli),cluster_size])
