"""Given an unsorted array of integers, find a 3-element subset that sums to zero. This is a special case of the SUBSET-SUM problem, which is NP-complete."""

import random
def  main():
	size = random.randint(1,1000)
	temp = []
	for i in range(size):
		temp.append(random.randint(1,1000))
	d = {}
	for elem in temp:
		d[elem] = elem
	for i in xrange(len(temp)):
		for j in xrange(len(temp)):
			sumx = (temp[i] + temp[j])
			if d.has_key(sumx):
				print temp[i], temp[j], d[sumx]
if __name__ == "__main__":
	main()
