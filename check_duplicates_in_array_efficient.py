"""I am trying to write an O(n) implementation to finding duplicate elements and list all elements that have been duplicates"""

"""The logic is to look at each element and store its occurence in a dictionary, if it allready exists and there is no key-errror, then the element is a duplicate."""

def duplicate_finder(num_list):
	hash_stuff = {}
	for i in num_list:
		try:
			temp = hash_stuff[i]
			if temp == 1:
				print str(i) + " is a duplicate"
				hash_stuff[i] = temp + 1
		except KeyError:
			hash_stuff[i] = 1

def main():
	duplicate_finder([2,3,1,0,2,5,3])
	
if __name__ == "__main__":
	main()
