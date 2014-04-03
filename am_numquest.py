def number(n):
	"""So the simplest logic in this case would be to find prime factors and then make the smallest number from among thses prime factors"""
	d = 2
	primefactors = []
	while(d*d <= n):
		while(n % d == 0):
			primefactors.append(d)
			n = n  / d
		d += 1
		
	if len(primefactors) > 1:
		sumt = 0
		if n > 1 and n < 10:
			primefactors.append(n)
		print primefactors
		for i in range(len(primefactors)):
			for j in range(i + 1, len(primefactors)):
				if primefactors[i] * primefactors[j] < 10 and primefactors[i] * primefactors[j] > 0:
					primefactors[i] = primefactors[i] * primefactors[j]
					primefactors[j] = 1
		
		print sorted(primefactors)
		print "Remove the one's and you have your god damn number"

	else:
		print -1	
def main():
	number(input())		

if __name__ == "__main__":
	main()
