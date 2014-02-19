def check_isomoorphs(string_one, string_two):
	tuples = [(string_two[i], string_one[i]) for i in range(len(string_one))]
	tuples = list(set(tuples))
	tuples_firsts = [i[0] for i in tuples]
	for i in tuples_firsts:
		if tuples_firsts.count(i)  > 1:
			print "Not Isomorphs"
			return 0
	print "Oh yeah, Nailed it"

def main():
	check_isomoorphs('app', 'foo')
	check_isomoorphs('bar', 'foo')
 	check_isomoorphs('turtle', 'tletur')
	check_isomoorphs('ab','ca')
main()
	
