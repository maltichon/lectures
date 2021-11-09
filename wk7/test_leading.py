# Example taken from Gries et al. 2013. Practical Programming: An Introduction
# to Computer Science Using Python 3

import unittest
import leading

class TestLeading(unittest.TestCase):
    '''Tests for leading'''

    def test_empty(self):
        '''Test an empty string.'''
        inputted = ''
        leading.leading_substrings(inputted)
        output_expected = ['']
        self.assertEqual(output_expected, inputted, "The string is empty.")

    def test_one(self):
        '''Test a one-character string'''
        inputted = 'a'
        leading.leading_substrings(inputted)
        output_expected = ['a']
        self.assertEqual(output_expected, inputted, "The string contains one character.")

    def test_two(self):
        '''Test a two-character string'''
        inputted = 'of'
        leading.leading_substrings(inputted)
        output_expected = ['o', 'of']
        self.assertEqual(output_expected, inputted, "The string contains two characters.")

    def test_three(self):
        '''Test a three-character string'''
        inputted = 'cat'
        leading.leading_substrings(inputted)
        output_expected = ['c', 'ca', 'cat']
        self.assertEqual(output_expected, inputted, "The string contains three characters.")


if __name__ == '__main__':
    unittest.main()
