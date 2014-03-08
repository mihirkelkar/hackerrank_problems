#!/usr/bin/python
from binary_tree import *

def bfs(self, root = None):
	queue = []
	root = self.root if root is None else root
	if self.root != None:
		queue.append(root)
	while queue:
		temp = queue.pop()
		print temp.value
		if temp.left != None:
			queue.append(temp.left)
		if temp.right != None:
			queue.append(temp.right)

binary_search_tree.bfs = bfs

def main():
	bst = binary_search_tree(0)
	for i in xrange(1,101):
		bst.add_node(i)
	bst.bfs()

if __name__ == "__main__":
	main()
	
	
	
	

