"""find out given domain names from a chunk of given html"""
"""Input format is an inteer n indicating the number of html chunks that will follow , followed by the actual html chunks"""
import re
link = []
def htmlmatcher(html):
	global link
	url = re.compile(r'href=\"https?://(.+)\"')
	temp_link = url.findall(html)
	for i in range(0, len(temp_link)):
		#yank of the www acronym
		temp_link[i] = re.sub(r'www.', r'', temp_link[i])
		
		#yank off any sub page attachments
		temp_link[i] = re.sub(r'/.+', r'', temp_link[i])
		
		#yank off java-script extension to things
		temp_link[i] = re.sub(r'\".+', r'', temp_link[i])
		
		link.append(temp_link[i])

def main():
	global link
	number = input()
	for i in range(0, number):
		htmlmatcher(raw_input())		
	
	#remove duplicates from the global list
	link = list(set(link))
	string = link[0]
	for i in range(1, len(link)):
		string = string + ';' + link[i]
	print string

if __name__ == "__main__":
	main()
