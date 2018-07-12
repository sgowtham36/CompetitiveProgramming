import unittest

alpha = {"A" :".-","B":"-...","C" :"-.-.","D" :"-..","E" :".","F" :"..-.","G" :"--.","H" :"....",
"I" :"..","J" :".---","K" :"-.-","L" :".-..","M" :"--",	"N" :"-.","O" :"---","P" :".--.","Q" :"--.-",
"R" :".-.","S" :"...","T" :"-","U" :"..-","V" :"...-","W" :".--","X" :"-..-","Y" :"-.--","Z" :"--.."}

def transformations(in_list):
	global alpha
	res = []
	for word in in_list:
		le = len(word)
		wo = ""
		for i in range(le):
			wo += alpha[word[i].upper()]
		res.append(wo)
	res = set(res)
	return len(res)



class Test(unittest.TestCase):

	def test_one(self):
		Input_words = ["gin", "zen", "gig", "msg"]
		output = 2
		ans = transformations(Input_words)
		self.assertEqual(ans,output)
	def test_two(self):
		Input_words = ["a", "z", "g", "m"]
		output = 4
		ans = transformations(Input_words)
		self.assertEqual(ans,output)
	def test_three(self):
		Input_words = ["bhi", "vsv", "sgh", "vbi"]  
		output = 3
		ans = transformations(Input_words)
		self.assertEqual(ans,output)
	def test_four(self):
		Input_words = ["a", "b", "c", "d"]  
		output = 4
		ans = transformations(Input_words)
		self.assertEqual(ans,output)
	def test_five(self):
		Input_words =  ["hig", "sip", "pot"]  
		output = 2
		ans = transformations(Input_words)
		self.assertEqual(ans,output)


unittest.main(verbosity=2) 