"""Given a string, rearrange the string to a palindrome and return the palindrome if present or -1""" 
def re_palindrome(string):
	string_map = {}
	odd_count = 0
	for i in string:
		try:
			temp = string_map[i]
			string_map[i] = temp + 1
		except:
			string_map[i] = 1
	freq_count = string_map.values()
	for value in freq_count:
		if value % 2 != 0:
			odd_count += 1
			if odd_count > 1:
				print "Nope! can't make a palindrome. Deal with it"
				return
	word_and_freq = string_map.items()
	word_and_freq = sorted(word_and_freq, key = lambda i: i[1])
	odd_words = [i for i in word_and_freq if i[1] % 2 != 0]
	even_words = [i for i in word_and_freq if i[1] % 2 == 0]
	odd_char = odd_words[0][0] * odd_words[0][1]
	even_char = ''
	for i in even_words:
		even_char += i[0] * (i[1] / 2)
	total_word = even_char + odd_char + even_char[::-1]
	print total_word
	print "So much palindrome. Such symmetry. wow"

	
def main():
	re_palindrome(raw_input("Enter the word to determine if you could make a palindrome"))

main()
	
