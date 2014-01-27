class node:
	def __init__(self, value):
		self.value = value
		self.ptr = None
class stack:
	elements = 0
	def push(self, value):
		if self.elements == 0:
			top = node(value)
			self.elements += 1
		else:
			temp = node(value)
			temp.ptr = top
			top = temp
			self.elements += 1
	def pop(self):
		print top.value
		top = top.ptr
		self.elements = self.elements - 1

	def print_stack(self):
		temp = top
		while(temp.ptr != None):
			print temp.value
			temp = temp.ptr

x = stack()
x.push(1)
x.push(2)
x.push(3)
x.pop()
