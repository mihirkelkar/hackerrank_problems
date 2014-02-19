def main():
	balance_paranthesis(raw_input("Enter the goddamm string"))


def balance_paranthesis(string):
	open = 0
	result = ''
	for char in string:
		if char == "(":
			open += 1
			result += char
		elif char == ")":
			if open > 1:
				result += char
				open -= 1
		else:
			result += char
	result += ( open * ')' )
	print result

if __name__ == "__main__":
	main()			 
