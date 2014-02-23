#!/usr/bin/python

class node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
class binary_search_tree:
	
	def __init__(self, value):
		temp = node(value)
		self.root  = temp
		print "Root created"

	def add_node(self,value,root = None):
		root = self.root if root is None else root
		"""So basically I need to pass the root each time to amke recursive calls, but I dont want to pass it from the main function call, so I set its default value to None and then just chekc if its None, if its I make it self.root. Pretty Neat"""
		if value < root.value:
			if root.left != None:
				self.add_node(value, root.left)
			else:
				temp = node(value)
				root.left = temp
				print "left child to node with value ", root.value, " created"
		elif value >= root.value:
			if root.right != None:
				self.add_node(value, root.right)
			else:
				temp = node(value)
				root.right = temp
				print "right child to node with value ", root.value, " created"

	def search_node(self, value, root = None):
		root = self.root if root is None else root
		""" Same trick I use above. I get the initial value as None and make it self.root for the first call in the above line"""
		if value == root.value:
			print "value found"
			return 
		elif value < root.value:
			if root.left != None:
				self.search_node(value, root.left)
			else:
				print "Vaue not found"
		elif value > root.value:
			if root.right != None:
				self.search_node(value, root.right)
			else:
				print "Value not found"

	def delete_node(self, value, root = None):
		root  = self.root if root is None else root
		if value == root.value:
			if(root.left != None) or (root.right != None):
				print "This node has a subtree, cannot delete it"
			else:
				print "Node found, will be deleted"
				return 1
		elif value < root.value:
			if root.left != None:
				temp = self.delete_node(value, root.left)
				if temp == 1:
					root.left = None
			else:
				print "Node to delete not found"
		elif value > root.value:
			if root.right != None:
				temp = self.delete_node(value, root.right)
				if temp == 1:
					root.right = None
			else:
				print "node to delete not found"		
	def pre_order(self, root = None):
		root = self.root if root is None else root
		print root.value
		if root.left != None:
			self.in_order(root.left)
		if root.right != None:
			self.in_order(root.right)

	def in_order(self, root = None):
		root  = self.root if root is None else root
		if root.left != None:
			self.in_order(root.left)
		print root.value
		if root.right != None:
			self.in_order(root.right)
		
	def post_order(self, root = None):
		root = self.root if root is None else root
		if root.left != None:
			self.post_order(root.left)
		if root.right != None:
			self.post_order(root.right)
		print root.value	
		
def main():
	bst = binary_search_tree(4)
	bst.add_node(1)
	bst.add_node(2)
	bst.add_node(3)
	bst.search_node(7)
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	bst.in_order()
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	bst.pre_order()
	print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	bst.post_order()

if __name__ == "__main__":
	main()
