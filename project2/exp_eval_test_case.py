import unittest
from StackArray import StackArray
from Node import Node
from exp_eval import *


class TestCase(unittest.TestCase):
    def test_infix_to_Postfix(self):
        string1 = '( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )'
        self.assertEqual(infix_to_postfix(string1), '5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^')
        string2 = '( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )'
        self.assertEqual(infix_to_postfix(string2), '15 7 1 1 + - / 3 * 2 1 1 + + -')
        string3 = '5 * 3 ^ ( 4 - 2 )'
        self.assertEqual(infix_to_postfix(string3), '5 3 4 2 - ^ *')
        string4 = '10 + 3 * 5 / ( 16 - 4 )'
        self.assertEqual(infix_to_postfix(string4), '10 3 5 16 4 - / * +')
        string5 = '( ( 1 * 2 ) + ( 3 / 4 ) )'
        self.assertEqual(infix_to_postfix(string5), '1 2 * 3 4 / +')
        string6 = '( ( 2 * ( 3 + 4 ) ) / 5 )'
        self.assertEqual(infix_to_postfix(string6), '2 3 4 + * 5 /')
        string7 = '( 3 * ( 4 + 6 / 3 ) )'
        self.assertEqual(infix_to_postfix(string7), '3 4 6 3 / + *')
        string8 = '~ 3 * 3 + 9'
        self.assertEqual(infix_to_postfix(string8), '3 ~ 3 * 9 +')
        string9 = '( ~ 3 ) ^ 2 + 9'
        self.assertEqual(infix_to_postfix(string9), '3 ~ 2 ^ 9 +')
        string10 = '4 ^ ( ~ 1 ) * 4'
        self.assertEqual(infix_to_postfix(string10), '4 1 ~ ^ 4 *')
        string11 = '~ 1'
        self.assertEqual('1 ~', infix_to_postfix(string11))
        string12 = '~ ~ 1'
        self.assertEqual('1 ~ ~', infix_to_postfix(string12))

    def test_post_fix_eval(self):
        string1 = '5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^'
        self.assertAlmostEqual(post_fix_eval(string1), 2.828427125)
        string2 = '5 3 4 2 - ^ *'
        self.assertAlmostEqual(post_fix_eval(string2), 45.0)
        string3 = '15 7 1 1 + - / 3 * 2 1 1 + + -'
        self.assertAlmostEqual(post_fix_eval(string3), 5.0)
        string4 = '10 3 5 16 4 - / * +'
        self.assertAlmostEqual(post_fix_eval(string4), 11.25)
        string5 = '1 2 * 3 4 / +'
        self.assertAlmostEqual(post_fix_eval(string5), 2.75)
        string6 = '2 3 4 + * 5 /'
        self.assertAlmostEqual(post_fix_eval(string6), 2.8)
        string7 = '3 4 6 3 / + *'
        self.assertEqual(post_fix_eval(string7), 18.0)
        string8 = '3 ~ 3 * 9 +'
        self.assertEqual(post_fix_eval(string8), 0.0)
        string10 = '4 1 ~ ^ 4 *'
        self.assertEqual(post_fix_eval(string10), 1.0)
        string11 = '1 ~'
        self.assertEqual(post_fix_eval(string11), -1)
        string12 = '1 ~ ~'
        self.assertEqual(post_fix_eval(string12), 1.0)
        string13 = '3 ~ 2 ^ 9 +'
        self.assertEqual(post_fix_eval(string13), 18.0)

    def test_postfix_valid(self):
        string1 = '1 1 + +'
        self.assertEqual(postfix_valid(string1), False)
        string2 = '15 7 1 1 + - / 3 * 2 1 1 + + -'
        self.assertEqual(postfix_valid(string2), True)
        string3 = '15 7 1 1 + - / 3 * 2 1 1 + + - ~'
        self.assertEqual(postfix_valid(string3), True)
        string4 = '3 ~ 2 9 +'
        self.assertEqual(postfix_valid(string4), False)
        string5 = '10 3 + 5 16 4 - / * +'
        self.assertEqual(postfix_valid(string5), False)
        string6 = "3 + ~ 3"
        self.assertEqual(postfix_valid(string6), False)

    def test_infix_valid(self):
        string1 = '3 ~ + 3'
        self.assertEqual(infix_valid(string1), False)
        string2 ='3 + ~ 3'
        self.assertEqual(infix_valid(string2), True)
        string3 = '3 + 3 ~'
        self.assertEqual(infix_valid(string3), False)
        #string4 = '15 7 1 1 + - / 3 * 2 1 1 + + -'
        #self.assertEqual(infix_valid(string4), False)


def main():
    unittest.main()


if __name__ == '__main__':
        main()