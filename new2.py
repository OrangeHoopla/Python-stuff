import urllib
import re
import time
nothing_rep = "and the next nothing is (\d+)"
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing = '8022'
while True:
	try:
		print nothing 
		source = urllib.urlopen(uri % nothing).read()
		nothing = re.search(nothing_rep, source).group(1)
	except:
		break

	    