import tweepy
import csv

#insert keys

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#tweets = api.user_timeline('comprehensive')

status =[]

csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)

def limit_handled(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			time.sleep(15 * 60)

for tweet in limit_handled(tweepy.Cursor(api.search,q = "comprehensive",since="2017-02-28",until="2017-09-29",lang="en").items(600)):
	print(tweet.text)
	status.append([tweet.text.encode('utf-8')])
	
for st in status:
	csvWriter.writerow(st)


csvFile.close()

