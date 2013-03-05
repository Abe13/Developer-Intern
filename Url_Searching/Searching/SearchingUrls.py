import twitter
import json
import time
import sys
import re

#Login in twitter

def takeUrl( text):
	s='[hH][tT][tT][pP][sS]?'
	s+=':'
	s+='//'
	s+='[^ ^\n^\#]+'

	f=re.compile(s)
	return f.findall(text)

def hashtag(Text):
	s='^\#'
	s+='[^ ^\#]+'
	f=re.compile(s)
	d=f.findall(Text)
	if d:
		return Text
	else:
		exit(0)
def unique(urls, text):
	for t in urls:
		if re.match(t.upper(),text.upper()):
			return False
	return True


try:
    Text=sys.argv[1]
    Term=hashtag(Text)

    print "Searching for: ",Term,"\n"
	
	consumer_secret='consumer_secret'
	consumer_key='consumer_key'
	access_token_key='access_token_key'
	access_token_secret='access_token_secret'
	
	
    api = twitter.Api(consumer_secret=consumer_secret,consumer_key=consumer_key,access_token_key=access_token_key,access_token_secret=access_token_secret)
    print"Twitter Authentication is done!\n"


    print "Pulling data from twitter...\n"

    tweets=api.GetSearch(term=Term, geocode=None, since_id=None, per_page=100, page=1, lang='en', show_user='true', query_users=False)
    urls=[]
    for t in tweets:
        for url in takeUrl(t.text):
			if (unique(urls,url)):
				if url[-1]=='.':

					urls.append(url[:-1])

				else:
					urls.append(url)




    print "URLs\n"
    for url in urls:
        print url.encode('ascii','ignore')
except:
    print "\nThere is an error in execution! "
    print "Likely you didn't provid hashtag!"
