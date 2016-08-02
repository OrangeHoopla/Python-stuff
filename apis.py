from urllib2 import *
request = Request('https://mycf.cf.edu/ics')
try:
	response = urlopen(request)
	test = response.read()
	print test
except URLError, e :
	print "try again kiddo", e
count = 0
if any in test == "cf" count = count + 1