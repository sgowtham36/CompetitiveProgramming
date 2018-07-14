import unittest

def hammerDistance(x,y):

	bin_x = bin(x)[2:].zfill(8)
	bin_y = bin(y)[2:].zfill(8)
	ans = []
	for i in range(7,-1,-1):
		if bin_x[i] != bin_y[i]:
			ans.append(7-i)
	return len(ans)

class Test(unittest.TestCase):

	def test_one(self):
		x = 25
		y = 30
		expected = 3
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)

	def test_two(self):
		x = 1
		y = 4
		expected = 2
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)
	def test_three(self):
		x = 25
		y = 30
		expected = 3
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)

	def test_four(self):
		x = 100
		y = 250
		expected = 5
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)
	def test_five(self):
		x = 1
		y = 30
		expected = 5
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)
	def test_six(self):
		x = 0
		y = 255
		expected = 8
		res = hammerDistance(x,y)
		self.assertEqual(res,expected)

unittest.main(verbosity=2)
