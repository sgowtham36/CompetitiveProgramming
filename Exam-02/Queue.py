import unittest


def reconstruction(in_list):
	inserted = []
	sl = sorted(in_list , key = lambda x : x[1])
	count = 0
	for i in sl:
		if i[1] == 0:
			count += 1
	res = sorted(sl[:count],key = lambda x:x[0])
	sl = sl[count:]
	# print(res)
	low = res[0][0]
	high = res[-1][0]
	sl = sorted(sl , key = lambda x : x[0])
	while len(sl)!=0:
		for i in range(len(sl)):
			if sl[i][0] <= low and sl[i][1] == len(res):
				low = sl[i][0]
				res.append(sl[i])
				sl = sl[:i]+sl[i+1:]
				break
			elif sl[i][0] <= high and sl[i][0] >= low:
				if low == high:
					low = sl[i][0]
				res.append(sl[i])
				sl = sl[:i]+sl[i+1:]
				break

	return res




class Test(unittest.TestCase):

	def test_one(self):
		Input_words = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
		output = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
		ans = reconstruction(Input_words)
		self.assertEqual(ans,output)
	def test_two(self):
		Input_words = [[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
		output = [[12,0],[11,1],[9,2],[6,3],[3,4],[1,5]]
		ans = reconstruction(Input_words)
		self.assertEqual(ans,output)
	def test_three(self):
		Input_words = [ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
		output = [[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]
		ans = reconstruction(Input_words)
		self.assertEqual(ans,output)


unittest.main(verbosity=2) 