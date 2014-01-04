import re
def id_comment():
	fp = open('testcase1', 'rU')
	testcase = fp.readlines()
	testcase = ''.join(testcase)
	#print testcase
	multi_line_comment = re.compile(r'/\*[\s\d\w\t\n\r{}~!@#$%^&*()_+=-`<>,.?;:|]+\*/')
	single_line_comment = re.compile(r'//.+')
	multi_lines = multi_line_comment.findall(testcase)
	single_lines = single_line_comment.findall(testcase)
	print '\n'.join(multi_lines)
	print '\n'.join(single_lines)


def main():
	id_comment()

if __name__ == "__main__":
	main()



	
