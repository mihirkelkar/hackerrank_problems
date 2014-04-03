#!/usr/bin/python
from binary_tree import *

def dfs(self, root = None):
	root = self.root if root is None else root
	if root != None:
		if root.left != None:
			self.dfs(root.left)
		if root.right != None:
			self.dfs(root.right)
		print root.value

	else:
		print "Nothing to print"

binary_search_tree.dfs = dfs

def main():
	bst = binary_search_tree(8)
	bst.add_node(3)
	bst.add_node(10)
	bst.add_node(1)
	bst.add_node(6)	
	bst.add_node(4)
	bst.add_node(7)
	bst.add_node(14)
	bst.add_node(13)
	bst.dfs()

if __name__ == "__main__":
	main()
