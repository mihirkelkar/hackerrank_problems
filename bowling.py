import unittest
from random import choice
class game:

	def __init__(self):
		self.frames_list = []

	def frame_number(self):
		return len(self.frames_list)
	def bowl_game(self):
	#	counter = 0
		for i in range(10):
			num1 = self.roll(0)
			if num1 == 10:
				self.frames_list.append(num1)
			else:
				num2 = self.roll(1)
				self.frames_list.append(num1 + num2)

			
	def roll(self, numPins):
		return 4

	def score(self):
		sum = 0
		for i in range(len(self.frames_list)):
			sum += self.frames_list[i]
		return sum
	
class testbowling(unittest.TestCase):
	
	def setUp(self):
		self.x = game()
	
	#def test_check_instance(self):
	#	x = game()

	def test_twenty_rolls(self):
		n = self.x.frame_number()
		self.assertEqual(n,0)
		self.x.bowl_game()
		self.assertEqual(self.x.frame_number(), 10)
		self.assertEqual(self.x.score(), 80)
	#def test_strike_skip(self):
	#	length = self.x.frame_number()
	#	self.assertEqual(self.x.frame_number(), 10) 
if __name__ == "__main__":
	unittest.main(verbosity = 2)
	
