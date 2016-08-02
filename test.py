words = []
for line in open('redditinfo.txt'):
	words = line.split() + words
info = words[1::2]
word = words[3]
print word

cache = []
for line in open('redditIds.txt'):
	cache = line.split() + cache

print cache

OutputFile = open("redditIds.txt", 'a')
OutputFile.write("\n" + "12")
for x in range(1,11):
	OutputFile.write("\n" + "%d" % (x))

