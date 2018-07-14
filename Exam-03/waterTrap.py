import unittest

def waterTrap(in_list):
	n = len(in_list)
	left = [0]*n
	right = [0]*n
	water = 0
	left[0] = in_list[0]
	for i in range( 1, n):
		left[i] = max(left[i-1], in_list[i])
	right[n-1] = in_list[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i+1], in_list[i]);
	for i in range(0, n):
		water += min(left[i],right[i]) - in_list[i]

	return water

class Test(unittest.TestCase):

	def test_one(self):
		in_list = [0, 1, 0, 2, 1, 0, 1]
		expected = 2
		res = waterTrap(in_list)
		self.assertEqual(res,expected)

	def test_two(self):
		in_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
		expected = 6
		res = waterTrap(in_list)
		self.assertEqual(res,expected)
	def test_three(self):
		in_list = [0, 1, 0, 2, 1, 0, 5, 1, 0, 2]
		expected = 7
		res = waterTrap(in_list)
		self.assertEqual(res,expected)

	def test_four(self):
		in_list = [0, 1, 0, 5, 1, 0, 2]
		expected = 4
		res = waterTrap(in_list)
		self.assertEqual(res,expected)
	def test_five(self):
		in_list = [0, 5, 1, 3, 4, 0, 1]
		expected = 5
		res = waterTrap(in_list)
		self.assertEqual(res,expected)


unittest.main(verbosity=2)