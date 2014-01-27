import itertools
"""Given "n" generate all valid parenthesis strings of length 2n"""
number = input()
string = '(' * number
string += ')' * number
for i in set(itertools.permutations(string)):
	temp = ''.join(i)
	open_count = 0
	close_count = 0
	flag = 0
	for j in temp:
		if open_count < close_count:
			flag = 1
			break
		else:
			if j == '(':
				open_count = open_count + 1
			elif j == ')':
				close_count = close_count + 1
	if flag == 1:
		continue
	else:
		print temp
	
	
		
