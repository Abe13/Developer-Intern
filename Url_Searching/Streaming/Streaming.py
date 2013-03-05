from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import re

consumer_secret='consumer_secret'
consumer_key='consumer_key'
access_token_key='access_token_key'
access_token_secret='access_token_secret'

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream.
	This is a basic listener that just prints received tweets to stdout.

	"""
	def __init__(self):
		self.tweets = []
		self.urls=[]
#		self.starttime = time.strftime("%d_%H_%M",time.localtime())

	def on_data(self, data):
		tweet = json.loads(data)
		print'[',len(self.tweets)+1,']-',tweet['text'].encode('ascii','ignore')

		self.tweets.append(tweet)
		for t in lis.takeUrl(tweet['text']):
		    if (lis.unique(t)):
				if t[-1]=='.':
					lis.urls.append(t[:-1])
				else:
					lis.urls.append(t)



		if len(self.tweets)>99:
			print "-----------------"
			return False

	def takeUrl(self, text):
		s='[hH][tT][tT][pP][sS]?'
		s+=':'
		s+='//'
		s+='[^ ^\n^\#]+'
		f=re.compile(s)
		return f.findall(text)

	def hashtag(self,Text):
		s='^\#'
		s+='[^ ^\#]+'
		f=re.compile(s)
		d=f.findall(Text)
		if d:
			return d
		else:
			return False
	def unique(self, text):
		for t in lis.urls:
			if re.match(t.upper(),text.upper()):
				return False
		return True






	def on_error(self, status):
		print status

	def on_timeout(self):
		print "timeout!"
		return False


try:


    lis = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    try:

    #	print 'Arg= ',sys.argv[:],'\n'
    	Text=sys.argv[1]

    except:
    	print "You didn't provid hashtag!"
    	Text=raw_input("Insert the word you're looking for\n")


    Term=lis.hashtag(Text)
    print "Searching for: ",Term[0]
    stream = Stream(auth, lis, timeout=1000)
    stream.filter(track=Term)

    print "URLs"
    for t in lis.urls:
        print t.encode('ascii','ignore')

except:
    print" \nThere is an error!"