#!/usr/bin/python
import mechanize
import re
def find():
	browser = mechanize.Browser()
	browser.addheaders = [('User-agent', 'Mozilla/5.0')]
	browser.set_handle_robots(False)
	html = browser.open("http://www.google.com/search?q=baltimore+temperature")
	html = ''.join([i if ord(i) < 128 else '' for i in html.read().lower()])
	match = re.search(ur'<span class="wob_t" style="display:inline">(\d+)[fc]</span>', html)
	if match:
		fp = open('temperature', 'a')
		fp.write(match.group(1) + "\n")
		fp.close()
	else:
		print "Something went wrong. Deal with it"

