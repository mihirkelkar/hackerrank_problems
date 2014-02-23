#!/usr/bin/python

class node:
	def __init__(self, value):
		self.value = value
		self.next = None
	
class linkedlist:
	def __init__(self):
		self.head = None
		self.tail = None
		self.counter = 0
	
	def add_node(self, value):
		x = node(value)
		if self.head == None:
			self.head = x
			self.tail = x
			self.counter += 1
		else:
			self.tail.next = x
			self.tail = x
			self.counter += 1
	def print_list(self):
		cur = self.head
		while(cur != None):
			print cur.value
			cur = cur.next

	def find_nth_element(self, n):
		if n > self.counter:
			"""%%% Checking to see if the element that we have picked aren't actually longer than the actual linkedlist"""
			print "This is impossible"
		else:
			npointer = self.head
			cur = self.head
			for i in range(0, n):
				npointer = npointer.next
			while(npointer != None):
				npointer = npointer.next
				cur = cur.next
			print "Element found ",
			print "The value of the element is", cur.value

				
def main():
	ll = linkedlist()
	for i in range(0, 100):
		ll.add_node(i)
	ll.print_list()
	print ll.head.value
	print ll.tail.value
	ll.find_nth_element(14)
if __name__ == "__main__":
	main()			
