class node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
class btree:
	
	def __init__(self):
		self.root = None
	
	def insert(self, value, root = None):
		root = self.root if root is None else root
		if root == None:
			root = node(value)
			self.root  = root

		else:
			if value < root.value:
				if root.left != None:
					self.insert(value, root.left)
				else:
					root.left = node(value)

			elif value >= root.right:
				if root.right != None:
					self.insert(value, root.right)
				else:
					root.right = node(value)



	def kpath(self, k, count = 0, root = None):
		root = self.root if root is None else root
		if root == None:
			print "The tree is empty"
		else:
			#Do a depth first search until you hit a leaf node. Check count at that position.
			#return true or false from that node.
			
			#In th parent node, if return is True, go ahead and delete the child
			count += root.value
			if root.left != None:
				ret = self.kpath(k, count, root.left)
				if ret == True:
					root.left = None
			if root.right != None:
				ret = self.kpath(k, count, root.right)
				if ret == True:
					root.right = None
			if root.left == None and root.right == None:
				if count < k:
					return True
				else:
					return False
					return False
			
				
			
	def printnode(self, root = None):
		root = self.root if root is None else root
		print root.value
		if root.left != None:
			self.printnode(root.left)
		if root.right != None:
			self.printnode(root.right)
def main():
	b = btree()
	for i in range(1, 16):
	b.printnode()
	b.kpath(20)
	b.printnode()
if __name__ == "__main__":
	main()	
