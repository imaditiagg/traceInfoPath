import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv


# Create a streamer object
class Listener(StreamListener):
    # When a tweet appears
    def on_status(self, status):
	csvFile = open('tweet stream1.csv', 'a')
        csvWriter = csv.writer(csvFile)

        try:
	       	csvWriter.writerow([status.text.encode('utf-8')])
        except Exception as e:
        	print(e)
                pass
	csvFile.close()
        return

    # When an error occurs
    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
 
    # When reach the rate limit
    def on_limit(self, track):
        print("Rate limited, continuing")
        return True

    # When timed out
    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        time.sleep(10)
	return

def status(queries):
	#insert keys

	listen = Listener()

    	auth = OAuthHandler(consumer_key, consumer_secret)
    	auth.set_access_token(access_token, access_token_secret)

    	stream = Stream(auth,listen)
	stream.filter(track=queries)

status(['wonderful'])
