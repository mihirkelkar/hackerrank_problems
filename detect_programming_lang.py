import re
"""Given a code from python,C or java. This code must be able to detect whether the given code is from what programming langugae by just using regular expressions. this also needs to be effective in space"""
#define regular expressions for Java
java = re.compile(r'import\s*java.?')
java_one = re.compile(r'public\s*class')

#define regular expressions for C programming

c = re.compile(r'#include<\w+\.h>')

#define regular expressions for python code
python = re.compile(r'print\s\"[\w\s\d\t\n\'\@\!\#\^\&\*\(\)\[\]\.\,\<\>\?\+\=\_\-\~\`\:\;]+\"')

def main():
	code = raw_input()
	match = java.search(code)
	if match:
		print "Java"
	else:
		match = java_one.search(code)
		if match:
			print "Java"
		else:
			match = c.search(code)
			if match:
				print "C"
			else:
				match = python.search(code)
				if match:
					print "Python"
if __name__ == "__main__":
	main()
