'''Given a roman numeral, convert it to an integer'''

class Solution(object):
    '''
            I   V   X   L   C   D   M
    value   1   5   10  50  100 500 1000
    '''

    def roman_to_int(self, s):
        '''
        keyword arguments:
        :type s - str
        :return type - int
        '''

        s = s.upper()
        convert_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        pre_letter_val = 2000

        for letter in s:
            cur_letter_val = convert_table[letter]

            if cur_letter_val <= pre_letter_val:
                val += cur_letter_val
                pre_letter_val = cur_letter_val
            else:
                sub = val % cur_letter_val
                val += cur_letter_val - 2 * sub

        return val
