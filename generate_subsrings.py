def substrings(string):
	if len(string)  > 1:
		temp = substrings(string[1:]) + substrings(string[:-1])
		return [string] + temp
	else:
		return [string]

def main():
	print ' '.join(list(set(substrings(raw_input("Enter your string")))))

if __name__ == "__main__":
	main()
