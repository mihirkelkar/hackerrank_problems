#!/usr/bin/python
import random
class node:
	def __init__(self,value):
		self.left = None
		self.right  = None
		self.value = value
	

class btree:
	def __init__(self):
		self.root = None

	def add_node(self, value, root = None):
		root = self.root if root is None else root
		if root == None:
			x = node(value)
			self.root = x
			print "Added root node"
		else:
			if value < root.value:
				if root.left != None:
					self.add_node(value, root.left)
				else:
					x = node(value)
					root.left = x
					print "Adding node to the left of node with value" + str(root.value)
			elif value >= root.value:
				if root.right != None:
					self.add_node(value, root.right)
				else:
					x = node(value)
					root.right = x
					print "Adding node to the right of th node with value" + str(root.value)

	def find_lowest_common_ancestor(self, value1, value2, root = None):
		root = self.root if root is None else root	
		if(value1 < root.value)and(value2 < root.value):
			self.find_lowest_common_ancestor(value1, value2, root.left)
		elif (value1 >= root.value) and (value2 >= root.value):
			self.find_lowest_common_ancestor(value1, value2, root.right)
		else:
			print "Found the lowest common ancestor, its the node with value " + root.value




def main():
	bst = btree()
	for i in range(1,100):
		bst.add_node(random.randint(1,100))
		

if __name__ == "__main__":
	main()			
