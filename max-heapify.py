#!/usr/bin/python
class node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class bsbtree:
	def __init__(self):
		self.root = None
	
	def addnode(self,value, root = None):
		root = self.root if root is None else root
		if root == None:
			temp = node(value)
			root = temp
		else:
			if value < root.value:
				if root.left != None:
					add_node(value, root.left)
				else:
					temp  = node(value)
					root.left = temp
			elif value >= root.value:
				if root.right != None:
					add_node(value, root.right)
				else:
					temp = node(value)
					root.right = temp
	
	def max_heapify(root):
		if root == null:
			return 
		else:
			left, right = float("-infinity")
			if root.left != None:
				left = max_heapify(root.left)	
			if root.right != None:
				right = max_heapify(root.right)
			if root.value < max(left, right):
				root.value = max(left, right)
			return root.value
			
 
