import unittest

def merge_ranges(array):
	max_val=0
	merge_list = [0] * 100

	for i in range(len(array)):
		x = array[i]
		if merge_list[x[0]] == 0:
			merge_list[x[0]]=x[1]
			max_val = max(max_val,x[1])
		elif merge_list[x[0]] < x[1]:
			merge_list[x[0]]=x[1]
			max_val = max(max_val,x[1])

	print(merge_list)

merge_ranges([1,2])

