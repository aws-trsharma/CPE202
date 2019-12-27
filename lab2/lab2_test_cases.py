import unittest 
from lab2 import perm_lex

class TestCase(unittest.TestCase):
     def test_perm_lex(self):
       string1 = 'abc'
       self.assertEqual(perm_lex(string1), ['abc','acb','bac', 'bca', 'cab', 'cba'])
       string2 = 'ab'
       self.assertEqual(perm_lex(string2), ['ab', 'ba'])
       string3 = 'abcd'
       self.assertEqual(perm_lex(string3), ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
def main():
       unittest.main()
if __name__ == '__main__':
        main()
