import unittest

def countingBits(in_list):
	res = []
	for i in range(in_list+1):
		bin_x = list(bin(i)[2:].zfill(8))
		li = [int(x) for x in bin_x]
		ans = sum(li)
		res.append(ans)
	return res

class Test(unittest.TestCase):

	def test_one(self):
		Input_words = 15
		output = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)
	def test_two(self):
		Input_words = 16
		output = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)
	def test_three(self):
		Input_words = 1
		output = [0, 1]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)
	def test_four(self):
		Input_words = 25 
		output = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2,3, 2, 3, 3, 4, 2, 3]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)
	def test_five(self):
		Input_words =  5
		output = [0, 1, 1, 2, 1, 2]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)
	def test_six(self):
		Input_words = 6 
		output = [0, 1, 1, 2, 1, 2, 2]
		ans = countingBits(Input_words)
		self.assertEqual(ans,output)


unittest.main(verbosity=2)