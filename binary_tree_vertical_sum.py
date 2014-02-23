#!/usr/bin/python
""" %%%% Calculate the vertical sum in a binary tree %%% """
class node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class binarytree:
	def __init__(self):
		self.root  = None
		self.vd = {}

	def add_node(self, value, counter =0 , root = None):
		root = self.root if root is None else root
		if root == None:
			temp = node(value)
			self.root = temp
			self.vd[counter] = value
			print counter, self.vd[counter]
			print "added 10"
		else:
			if value < root.value:
				if root.left != None:
					self.add_node(value, counter - 1, root.left)
				else:
					temp = node(value)
					root.left = temp
					try:
						self.vd[counter - 1] += value
						print counter - 1, self.vd[counter - 1]
					except:
						print "Setting value"
						self.vd[counter - 1] = value
						print counter - 1, self.vd[counter - 1]
					#print "added node to left of node having value", root.value
					
			elif value >= root.value:
				if root.right != None:
					self.add_node(value, counter + 1, root.right)
				else:
					temp = node(value)
					root.right = temp
					try:
						self.vd[counter + 1] += value
						print counter + 1, self.vd[counter + 1]
					except:
						print "Setting value"
						self.vd[counter + 1] = value
						print counter + 1, self.vd[counter + 1]
					#print "added node to right of node having value", root.value
	
				
		
def main():
	b = binarytree()
	b.add_node(10)
	b.add_node(8)
	b.add_node(12)
	b.add_node(7)
	b.add_node(9)
	b.add_node(11)
	b.add_node(13)
	print b.vd
if __name__ == "__main__":
	main()
