import sys
import re
answers = []
def needle_finder(i):
	global answers
	try:
		temp = re.search(i[1], i[2]).start()
		print temp
		answers.append(temp)
		while temp != None:
			string = i[:temp] + ' ' * i[0] + i[:temp + i[0]]
			if re.search(i[1], string):
				temp = re.search(i[1], string).start()
				answers.append(temp)
				print temp
			else:
				temp = None
			
	except:
		answers.append("\n")



def main():
	global answers
	x = sys.stdin
	rl = x.readline
	inputs = []
	while True:
		len_n = rl()
		needle = rl()
		hay_stack = rl()
		if len_n == '\n' or needle == '\n' or hay_stack == '\n':
			break
		else:
			temp = []
			temp.append(len_n)
			temp.append(needle)
			temp.append(hay_stack)
			inputs.append(hay_stack)
			
	for i in inputs:
		needle_finder(i)
	for i in answers:
		print i

if __name__ =="__main__":
	main()
