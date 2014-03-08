#!/usr/bin/python
#LONGEST PPEFIX MATCHING. 
"""So basically given a dictionary and a set of words, find the word which is the longest prefix of hte word which is a word in the given dictionary. """
"""The idea here is to build a trie tree. Each node od the tree contains a given value, and a dictionary of words which derive from the value + dict key.

eg  node = char = a , then it has a dictionary to all possible next chars, each representing a node, so b: node represents a node for all prefixes ab

the node ab, now has a char of 'ab' and a dictionary {a: node, b : node} each respectively representing words with prefixes aba and abb """
class node:
	def __init__(self, char = None):
		self.char = '' if char is None else char
		self.dict = {} #this dict looke like char : [list of nodes with next char as]


class tri_tree:
	def __init__(self):
		self.listlong = []
		self.root = node()
		self.flag = 0
		"""This is extremely important, the boolean lets us recognize is the given node is also a dictionary word is also an dictionary word. Example, the word child and children in the same dictionary will have the same tri-tree path , so the longest prefix match for child will be easily identified as a dictionary word by flag  = 1 , and word prefizes like 'chad' which are a valid path in the tri_tree but not actually in the dictionary will be returned as not a match"""

		print "root created"

	def add_node(self, word, root = None):
		root = self.root if root is None else root
		if len(word) > 0:
			try:
				temp = root.dict[word[0]]
				self.add_node(word[1:], temp)
			except:
				char = root.char  + word[0]
				root.dict[word[0]] = node(char)
				print "node added"
				self.add_node(word[1:], root.dict[word[0]])
				
		else:
			root.flag = 1

	def find_match(self, word, root = None):
		root = self.root if root is None else root
		if len(word) > 0:
			try:
				temp = root.dict[word[0]]
				print root.char
				if len(word) != 1:
					self.find_match(word[1:], temp)
				elif len(word) == 1:
					self.word_match(word[0], temp)
				if root.flag == 1:	
					print "match found, it is" + root.char	
					sys.exit(1)
					
								
			except:
				pass
		
def main():
	tt = tri_tree()
	tt.add_node("mihir")
	print "------------------------------"
	tt.add_node("mihit")
	tt.find_match("mihir")
if __name__ == "__main__":
	main()
		

