import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    n = len(sentence)
    li = []
    ind = 0
    for i in range(n):
        if sentence[i] == "(":
            if i == opening_paren_index:
                li.append(sentence[i])
                ind = len(li)
            else:
                li.append(sentence[i])
        elif sentence[i] == ")":
            if len(li) == ind:
                return i
            else:
                li.pop()
    if 1:
        raise ValueError("Bad input! Can't delete tail node.")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)