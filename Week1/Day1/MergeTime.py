import unittest

def merge_ranges(array):
	max_val=0
	merge_list = [0] * 100
	ans = []

	for i in range(len(array)):
		x = array[i]
		if merge_list[x[0]] == 0:
			merge_list[x[0]]=x[1]
			max_val = max(max_val,x[1])
		elif merge_list[x[0]] < x[1]:
			merge_list[x[0]]=x[1]
			max_val = max(max_val,x[1])
	x = 0
	first = False
	for i in range(max_val+2):
		# print(i)
		if merge_list[i] != 0:
			# print(x,i)
			if x == 0:
				if i == 0:
					first = True
				x = i
				# print(x)
		else:
			if x == 0 and first:
				ans.append((x,max(merge_list[x:i])))
				x = 0
				first = False
			elif x != 0:
				# print(x,i)
				ans.append((x,max(merge_list[x:i])))
				x = 0
	y=0
	for i in range(len(ans)):
		y = ans[i][0]




	print(ans)
	return ans

# Tests

class Test(unittest.TestCase):

   def test_meetings_overlap(self):
       actual = merge_ranges([(1, 3), (2, 4)])
       expected = [(1, 4)]
       self.assertEqual(actual, expected)

   def test_meetings_touch(self):
       actual = merge_ranges([(5, 6), (6, 8)])
       expected = [(5, 8)]
       self.assertEqual(actual, expected)

   def test_meeting_contains_other_meeting(self):
       actual = merge_ranges([(1, 8), (2, 5)])
       expected = [(1, 8)]
       self.assertEqual(actual, expected)

   def test_meetings_stay_separate(self):
       actual = merge_ranges([(1, 3), (4, 8)])
       expected = [(1, 3), (4, 8)]
       self.assertEqual(actual, expected)

   def test_meetings_not_sorted(self):
       actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
       expected = [(1, 4), (5, 8)]
       self.assertEqual(actual, expected)

   def test_sample_input(self):
       actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
       expected = [(0, 1), (3, 8), (9, 12)]
       self.assertEqual(actual, expected)


unittest.main(verbosity=2)

