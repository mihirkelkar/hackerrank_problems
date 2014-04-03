import sys
def find(array):
	print array
	if len(array) == 1:
		return array[0]
	else:
		if(array[0] + find(array[1:])) == 0:
			print "Yes"
			sys.exit(1)
		if(array[0] - find(array[1:])) == 0:
			print "Yes"
			sys.exit(1)
		print "Nope"

def main():
	find([1,2,3])
	
main()
