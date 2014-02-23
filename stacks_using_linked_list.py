#!/usr/bin/python
"""%%%%%%%%%%%%%%%%%%%--IMPLEMENTING STACK USING LINKED LIST--%%%%%%%%%%%%"""

class node:
	
	def __init__(self, value):	
		self.value = value
		self.next = None
		

class linked_list:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self,value):
		if self.head == None:
			x = node(value)
			self.head = x
			self.tail = x
		else:
			x = node(value)
			self.tail.next = x
			self.tail = x

class stack:
	def __init__(self):
		self.ll = linked_list()
	
	def push(self, value):
		self.ll.add_node(value) 
		print "%%%%%% PUSH OPS %%%%%%%%%%%%"
		self.show_stack(self.ll.head)	
	
	def pop(self):
		if self.ll.head != None:
			temp = self.ll.tail
			if self.ll.tail == self.ll.head:
				self.ll.head = None 
				self.ll.tail = None
			else:
				cur = self.ll.head
				while(cur.next != self.ll.tail):
					cur = cur.next
				self.ll.tail = cur
				self.ll.tail.next = None
			print "%%% POP OPS %%%"
			self.show_stack(self.ll.head)
			print "%%% RETURN OPS VALUE%%%"
			return temp.value
		else:
			print "%%% RETURN OPS VALUE %%%"
			print "Dude, its empty"	
			return None

	def show_stack(self, node):
		if node == None:
			print "Nothing to print, its an empty stack"
			return 
		elif node.next != None:
			self.show_stack(node.next)
		print node.value
		

def main():
	x = stack()
	x.push(1)	
	x.push(2)
	print x.pop()
	print x.pop()
	print x.pop()
	x.push(32)
	x.push(12)
if __name__ == "__main__":
	main()
