"""In a given array find all pairs of numbers which have a specified differnece between them"""


import math
def find_pairs(array, number):
	array.sort()
	res = 0
	for i in array[:-1]:
		print i
		if bin_search(array[array.index(i) + 1:], number + i):
			print "Update shit"
			res += 1
	return res

def bin_search(temp, number):
	print temp
	if len(temp) == 1:
		if temp[0] == number:
			print "Found it"
			return True
	else:
		mid = int(math.floor(float(0 + len(temp)) / 2.0))
		if number < temp[mid]:
			return bin_search(temp[:mid], number)
		elif number >= temp[mid]:
			return bin_search(temp[mid:], number)
def main():
	array = [1,2,3,4,5,6,7,8,9,10,11]
	number = 9
	print find_pairs(array, number)
	
if __name__ == "__main__":
	main()
		
