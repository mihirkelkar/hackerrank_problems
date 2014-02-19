import re
def checker(alien_language, tcases):
	answers = []
	for i in tcases:
		i = i.replace('(', '[')
		i = i.replace(')', ']')
		count = 0
		for j in alien_language:
			match = re.search(i, j)
			if match:
				count += 1
		answers.append(count)
	return answers

def main():
	fp = open('A-large-practice.in', r'U')
	op = open('output', 'w')
	inputs = [int(x) for x in (fp.readline().strip()).split()]
	alien_language = []
	tcases = []
	for i in range(inputs[1]):
		alien_language.append(fp.readline().strip())
	#print inputs
	#print "\n"
	#print alien_language
	for i in range(inputs[2]):
		tcases.append(fp.readline().strip())
	answers = checker(alien_language, tcases)
	for i in range(len(answers)):
		op.write("Case #" + str(i + 1) +":" + " "+str(answers[i]) + '\n')

if __name__ == "__main__":
	main()
