#!/usr/bin/python

class node:
	def __init__(self, value):
		self.value = value
		self.next = None

class singly_linked_list:
	
	def __init__(self):
		self.head = None
		self.tail = None
	def add_node(self, value):
		if self.head == None:
			x = node(value)
			self.head = x
			self.tail = x
		else:
			x = node(value)
			self.tail.next = x
			self.tail = x

	def print_list(self):
		cur  = self.head
		while(cur != None):
			print cur.value, 
			cur = cur.next

	def delete_element(self, value):
		#check if head has the value
		if self.head.value == value:
			print "Node found"
			self.head = self.head.next
		else:
			cur = self.head
			while(cur.next != None):
				if cur.next.value == value:
					print "Node found"
					cur.next = cur.next.next
					if cur.next == None:
						self.tail = cur
					return
				else:
					cur = cur.next
			print "Node not found"
				
	def reverse_print():
		self.head.print_reverse()
		
def main():
	x = singly_linked_list()
	x.add_node(2)
	x.add_node(3)
	x.add_node(4)
	x.print_list()
	x.delete_element(4)
	x.print_list()
	print "\n"
	x.add_node(5)
	x.print_list()
	print "\n"
	x.delete_element(3)
	x.print_list()
	x.delete_element(2)
	print("\n")
	x.print_list()
	print "\n"
	print x.head.value
	print x.tail.value
	x.add_node(1)
	x.add_node(2)
	x.add_node(3)
	x.add_node(4)
	x.reverse_print()
if __name__ == "__main__":
	main()	
