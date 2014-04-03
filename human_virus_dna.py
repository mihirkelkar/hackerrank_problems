"""Oh!! Mankind is in trouble again.This time its a deadly disease spreading at a rate never seen before. Efficient detectors for the virus responsible is the need of the hour. You are the lead at Central Hospital and need to find a fast and reliable way to detect the ‘foot-prints’ of the virus DNA in that of patient.

The DNA of the patient as well as of the virus consists of lower case letters. Since the data collected is raw there may be some errors. You will need to find all substrings in the patient DNA that exactly matches the virus DNA with the exception of at most one mismatch.

For example tolerating at most one mismatch, “aa” and “aa” are matching, “ab” and “aa” are matching, while “ab” and “ba” are not.

Input:
The first line contains the number of test cases T. T cases follow. Each case contains two lines containing strings P(Patient DNA) and V(Virus DNA) . Each case is followed by a blank line.

Output:
Output T lines, one corresponding to each case. For each case, output a space delimited list of starting indices (0 indexed) of substrings of P which are matching with V according to the condition mentioned above . The indices has to be in increasing order.

Constraints:
1 <= T <= 10
P and V contain at most 100000 characters each.
All characters in P and V are lowercase letters.

Sample Input:
3
abbab
ba

hello
world

banana
nan

Sample Output:
1 2

0 2

Explanation:
For the first case, the substrings of P starting at indices 1 and 2 are “bb” and “ba” and they are matching with the string V which is “ba”.
For the second case, there are no matching substrings so the output is a blank line.Find the part of the virus sub string that is a part of the human dna substring with the exception of one mismatch"""

def get_input():
	num = input()
	dna_list = []
	for i in range(0, num):
		human_dna = raw_input()
		virus_dna = raw_input()
		space = raw_input()
		dna_list.append((human_dna, virus_dna))
	return dna_list

def match_dna(i, j, orig_index, error_count, human_dna, virus_dna):
	if(human_dna[i] != virus_dna[j]):
	#if both charecters dont match
		if error_count == 0:
		#if this is the first error,
			error_count += 1
			if j < len(virus_dna) - 1:
				match_dna(i + 1, j + 1, orig_index, error_count, human_dna, virus_dna)
			# let it pass, make a recursive call to i + 1 and  j + 1 and  update error count given this is not he end of the virus substring
			elif j == len(virus_dna) - 1:
				print i - j, 
		#if this is the end of the virus substring, just print it
				error_count = 0
			#set error_count to 0
				orig_index = orig_index + 1
			#set orig_count + 1
				if orig_index < len(human_dna) - len(virus_dna) + 1:
						match_dna(orig_index, 0, orig_index, error_count, human_dna, virus_dna)
			#check if orig < len(human) - virus + 1
		elif error_count > 0:
		#if this is not the first error, 
			orig_index = orig_index + 1
			#incrment orig_index by 1
			error_count = 0
			#set error count to zero
			if orig_index < len(human_dna) - len(virus_dna) + 1:
				match_dna(orig_index, 0, orig_index, error_count, human_dna, virus_dna)
	
			#then make a recursive call to orig index and j is 0. also check if i < len(human_dna) - len(virus_dna) + 1
	elif human_dna[i] == virus_dna[j]:
	#if both charecters do match
		if j < len(virus_dna) - 1:
		#if this is not the end of the virus substring
			match_dna(i + 1, j + 1, orig_index, error_count, human_dna, virus_dna)
			# make a recursive call to i + 1 and j + 1
		if j == len(virus_dna) - 1:
			print i - j,
		#if this is the end of the virus string
			#print it
			error_count = 0
			#set error_count to 0
			orig_index = orig_index + 1
			#set orig_count + 1
			if orig_index < len(human_dna) - len(virus_dna) + 1:
				match_dna(orig_index, 0, orig_index, error_count, human_dna, virus_dna)
	
		
def main():
	dna_list = get_input()
	for i in dna_list:
		match_dna(0, 0, 0, 0, i[0], i[1])
		print "\n"
if __name__ == "__main__":
	main()
