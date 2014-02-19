totalcases = input()
for i in range(totalcases):
	temp = input()
	strings = []
	inputs = []
	for i in range(temp):
		inputs.append(raw_input())
		strings = strings + inputs[-1].split()
	print(list(set(strings)))

