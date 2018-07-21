import unittest

def binaryGap(n):
	y=bin(n)
	d=1
	mi=0
	fl=0
	if(n>0):
		y=y[2:]
	else:
		y=y[3:]
	for i in y:
		if(int(i)==1):
			fl+=1
			if(d>mi):
				mi=d
			d=1
		else:
			d+=1
	if(fl>=2):
		return mi
	else :
		return 0

class Test(unittest.TestCase):

	def test_one(self):
		Input_words = 0
		output = 0
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)
	def test_two(self):
		Input_words = 55
		output = 2
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)
	def test_three(self):
		Input_words = -5
		output = 2
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)
	def test_four(self):
		Input_words = 12354  
		output = 6
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)
	def test_five(self):
		Input_words =  6
		output = 1
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)
	def test_six(self):
		Input_words = 256 
		output = 0
		ans = binaryGap(Input_words)
		self.assertEqual(ans,output)


unittest.main(verbosity=2) 