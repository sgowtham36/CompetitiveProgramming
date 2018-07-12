import unittest

def find_duplicate(list):
    n = len(list)
    i = n
    j = n
    while True:
        i = list[i - 1]
        j = list[j - 1]  
        j = list[j - 1] 
        if i == j:
            break
    j = n
    while True:
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
            break
    return i

# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)