import unittest

def is_anagram(s,t):
	s = s.replace(' ','')
	t = t.replace(' ','')
	if (len(s)==len(t) ):
		# print(list(s))
		arr1 = list(s.lower())
		arr2 = list(t.lower())
		arr1.sort()
		arr2.sort()
		for i in range(len(s)):
			if arr1[i] != arr2[i]:
				return False
		return True
	else:
		return False

class Test(unittest.TestCase):

	def test_one(self):
		s = "anagram"
		t = "nagaram"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_two(self):
		s = "Keep"
		t = "Peek"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_three(self):
		s = "Mother In Law"
		t = "Hitler Woman"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_four(self):
		s = "School Master"
		t = "The Classroom"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_five(self):
		s = "ASTRONOMERS"
		t = "NO MORE STARS"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_six(self):
		s = "Toss"
		t = "Shot"
		ans = is_anagram(s,t)
		self.assertFalse(ans)
	def test_seven(self):
		s = "joy"
		t = "enjoy"
		ans = is_anagram(s,t)
		self.assertFalse(ans)
	def test_eight(self):
		s = "Debit Card"
		t = "Bad Credit"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_nine(self):
		s = "SiLeNt CAT"
		t = "LisTen AcT"
		ans = is_anagram(s,t)
		self.assertTrue(ans)
	def test_ten(self):
		s = "Dormitory"
		t = "Dirty Room"
		ans = is_anagram(s,t)
		self.assertTrue(ans)


unittest.main(verbosity=2)