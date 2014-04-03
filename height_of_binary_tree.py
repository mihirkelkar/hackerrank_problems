#!usr/bin/python
from binary_tree import *

def height_of_binary_tree(self, root):
	if root = None:
		return 0
	else:
		return (1 + max(height_of_binary_tree(root.left) + height_of_binary_tree(root.right)))


binary_search_tree.height_of_binary_tree = height_of_binary_tree

def main():
	bst = binary_search_tree(8)
	bst.add_node(3)
	bst.add_node(10)
	bst.add_node(1) 
	
	
