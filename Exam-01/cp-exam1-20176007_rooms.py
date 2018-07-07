import unittest

def room_keys(li):
	ans = [0]
	for i in range(len(li)):
		if i in ans:
			open_rooms(i,li,ans)
	ans = set(ans)
	if len(ans) == len(li):
		return True
	else:
		return False 
def open_rooms(x,li,ans):
	for j in li[x]:
		if j < len(li):
			ans.append(j)


class Test(unittest.TestCase):

	def test_one(self):
		s = [[1],[0,2],[3]]
		ans = room_keys(s)
		self.assertTrue(ans)
	def test_two(self):
		s = [[1,3], [3,0,1], [2], [0]]
		ans = room_keys(s)
		self.assertFalse(ans)
	def test_three(self):
		s = [[1,2,3], [0], [0], [0]]
		ans = room_keys(s)
		self.assertTrue(ans)
	def test_four(self):
		s = [[1], [0,2,4], [1,3,4], [2], [1,2]]
		ans = room_keys(s)
		self.assertTrue(ans)
	def test_five(self):
		s = [[1], [2,3], [1,2], [4], [1], [5]]
		ans = room_keys(s)
		self.assertFalse(ans)
	def test_six(self):
		s = [[1], [2], [3], [4], [2]]
		ans = room_keys(s)
		self.assertTrue(ans)
	def test_seven(self):
		s = [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]
		ans = room_keys(s)
		self.assertFalse(ans)



unittest.main(verbosity=2)