""" %%% Start with a standard doubly linked list. Now Imagine that in addition to the next and previous pointer , each element has a child pointer , which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on to produce a multilevel data structure 

The data structure I am trying to make looks like this

5  ->  33  ->  17  ->  2  ->  1 
|		       | 	
6  ->  25  ->  6       2  ->  7
       |       |       |       
       8       9       12 ->  5
	       |       | 
	       7       21 ->  3




and then flatten it out like a normal linked list
"""

"""----------THIS PART IS ACTUALLY NOT THE SOLUTION, I AM JUST CONSTRUCTING THE DATA STRUCTURE SO THAT I CAN FLATTEN IT LATER. THE END OF THE DATA STRUCTURE WILL BE DENOTED BY A SIMILAR COMMENT WITH DOTTED LINES----------------"""
class node:
	
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
		self.child = None
	
class linkedlist:
	
	def __init__(self):
		self.head = None
		self.tail = None
	
	def add_node(self, value):
		temp = node(value)
		if self.head == None:
			self.head = temp
			self.tail = temp
		else:
			self.tail.next = temp
			temp.prev = self.tail
			self.tail = temp
	def add_child(self,value, root):
		if root.child == None:
			x = node(value)
			root.child = x
		else:
			root = root.child
			while(root.next != None):
				root = root.next
			x = node(value)
			root.next = x
			x.prev = root
	
	def print_list(self, root):
		if root != None:
			print root.value
			if root.child != None:
				print "Accesing Child Element"
				self.print_list(root.child)
			self.print_list(root.next)

	def flatten_list(self):
		"""%%% THE SOLUTION %%%"""
		"""" MY LOGIC FOR DOING THIS THING IS AS FOLLOWS   
			while not at end of list:
				if you have a child, append the child to end of list
				(Don't worry if that cihld has children or the child has a next. Since it gets added to the end, thy automatically get taken care of sometime later)
		"""
		cur = self.head
		while(cur != None):
			if cur.child != None:
				cur.child.prev = self.tail
				self.tail.next = cur.child
				temp = cur.child
				while(temp.next != None):
					temp = temp.next
				self.tail = temp	
			cur = cur.next

		cur = self.head
		while(cur != None):
			print cur.value
			cur = cur.next
		print "%%%% FUCK YEAH %%%"

		

def main():
	x = linkedlist()
	x.add_node(5)
	x.add_child(6, x.tail)
	x.add_child(25, x.tail)
	x.add_child(6, x.tail) 
	x.add_child(8, x.tail.child.next)
	x.add_child(9, x.tail.child.next.next)
	x.add_child(7, x.tail.child.next.next.child)
	x.add_node(33)
	x.add_node(17)
	x.add_node(2)
	x.add_child(2, x.tail)
	x.add_child(7, x.tail)
	x.add_child(12, x.tail.child)
	x.add_child(5, x.tail.child)
	x.add_child(21, x.tail.child.child)
	x.add_child(3, x.tail.child.child)
	x.add_node(1)
	x.print_list(x.head)
	print x.head.value, "is the head pointer value"
	print x.tail.value,  "is the tail pointer value"
	print "%%%%%%%% FLATTENING THE BLOODY LIST %%%%%%%%%%%%%"
	x.flatten_list()

if __name__ == "__main__":
	main()
			
