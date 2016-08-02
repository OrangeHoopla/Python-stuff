import praw 
import time
import sqlite3


r = praw.Reddit(user_agent = "Tutorial bot /u/Creative_Name124")
words = []
for line in open('redditinfo.txt'):
	words = line.split() + words
Username = words[1]
Password = words[3]
r.login(Username, Password)
words_to_match = ["kno"]


sql = sqlite3.connect("sql.db")
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(ID TEXT)')
sql.commit()

OutputFile = open("redditIds.txt", 'a+')
for line in OutputFile:
	cache = line.split() + cache





def run_bot():
	subreddit = r.get_subreddit("test")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		cur.execute('SELECT * FROM oldposts WHERE ID = ?', [comment.id])
		if not cur.fetchone():
			comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if isMatch:
			cur.execute('INSERT INTO oldposts VALUES(?)',[comment.id])
			print("match found id:" + comment.id)
			comment.reply("Hello I'm a bot")

			
		
		
			

while True:
	run_bot()
	time.sleep(10)
