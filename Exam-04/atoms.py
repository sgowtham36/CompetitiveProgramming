import unittest
from collections import Counter
import re

class Solution(object):
    RE = re.compile(
        r'(?P<atom>[A-Z][a-z]*)(?P<atom_count>\d*)|'
        r'(?P<new_group>\()|'
        r'\)(?P<group_count>\d*)|'
        r'(?P<UNEXPECTED_CHARACTER_IN_FORMULA>.+)'
    )
    @classmethod
    def atom_count(cls, stack, atom, atom_count='', **_):
        stack[-1][atom] += (1 if atom_count == '' else int(atom_count))

    @classmethod
    def new_group(cls, stack, **_):
        stack.append(Counter())

    @classmethod
    def group_count(cls, stack, group_count='', **_):
        group_count = 1 if group_count == '' else int(group_count)
        group = stack.pop()
        for atom in group:
            group[atom] *= group_count
        stack[-1] += group

    @classmethod
    def countOfAtoms(cls, formula):
        stack = []
        cls.new_group(stack)
        for m in cls.RE.finditer(formula):
            getattr(cls, m.lastgroup)(stack, **m.groupdict())
        return ''.join(
            atom + (str(count) if count > 1 else '')
            for atom, count in sorted(stack.pop().items())
        )

class Test(unittest.TestCase):

    def test_one(self):
        Input_words = "H2O"
        output = "H2O"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_two(self):
        Input_words = "Mg(OH)2"
        output = "H2MgO2"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_three(self):
        Input_words = "K4(ON(SO3)2)2"
        output = "K4N2O14S4"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_four(self):
        Input_words = "C10H16O"
        output = "C10H16O"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_five(self):
        Input_words =  "Zn(NO3)2"
        output = "N2O6Zn"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_six(self):
        Input_words = "NaOH"
        output = "HNaO"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)
    def test_seven(self):
        Input_words = "F2"
        output = "F2"
        ans = Solution.countOfAtoms(Input_words)
        self.assertEqual(ans,output)



unittest.main(verbosity=2)