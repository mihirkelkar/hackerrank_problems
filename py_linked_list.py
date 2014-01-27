class node:
	def __init__(self, value):
		self.value = value
		self.nxtptr = None
	def append(self, somenode):
		self.nxtptr = somenode

head = node(0)
tail = head

for i in range(1, 100):
	temp = node(i)
	tail.append(temp)
	tail = tail.nxtptr

tempptr = head
while(tempptr != None):
	print tempptr.value
	tempptr = tempptr.nxtptr
