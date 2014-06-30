#!/usr/bin/python

class Node(object):
  def __init__(self, value):
    self.value = value
    self.bottom = None

class Stack(object):
  def __init__(self):
    self.top = None

  def push(self, value):
    if self.top == None:
      self.top = Node(value)
    elif self.top != None:
      new_node = Node(value)
      new_node.bottom = self.top
      self.top = new_node

  def pop(self):
    if self.top != None:
      retval = self.top.value
      self.top = self.top.bottom
      return retval
    else:
      print 'Stack Empty'
      return None

  def peek(self):
    if self.top != None:
      return self.top.value
    else:
      return None
  
  def isEmpty(self):
    if self.top == None:
      return True
    else:
      return False

  def print_stack(self, cur = None):
    cur = self.top if cur is None else cur
    if cur != None:
      print cur.value
      print '-------'
      if cur.bottom != None:
        self.print_stack(cur.bottom)

def infix_to_postfix(expression):
  result = ''
  Stack_one = Stack()
  pdict = {'^' : 1, '*' : 2, '/': 2, '%' : 2, '+': 3, '-': 3}
  for i in expression:
    if i not in '+-()*/^%':
      result += i
    else:
      if Stack_one.isEmpty() or i == '(':
        Stack_one.push(i)
      else:
        if i == ')':
          while True:
            char = Stack_one.pop()
            if char == '(':
              break
            else:
              result += char
        else:
          cur = Stack_one.top 
          while(cur != None and (pdict[cur.value] <= pdict[i])):
            result += Stack_one.pop()
            cur = Stack_one.top
          Stack_one.push(i) 
  if Stack_one.isEmpty():
    pass
  else:
    while not Stack_one.isEmpty():
      result += Stack_one.pop()
  print result
      
def main():
  infix_to_postfix('a+b*c-d')
if __name__ == '__main__':
  main()
