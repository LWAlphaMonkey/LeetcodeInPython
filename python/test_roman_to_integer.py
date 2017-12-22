import unittest
from roman_to_integer import Solution

class RomanToIntegerTesttMethods(unittest.TestCase):
    def test_roman_to_int(self):
        s = Solution()
        self.assertEqual(s.roman_to_int('MDCDIII'), 1903, 'MDCDIII is 1903')
        self.assertEqual(s.roman_to_int('XIIX'), 18, 'XIIX is 18')
        self.assertEqual(s.roman_to_int('MDCCCCX'), 1910, 'MDCCCCX is 1910')

if __name__ == '__main__':
    #verbosity 0(quiet), 1(default), 2(verbose)
    unittest.main(verbosity=2)
