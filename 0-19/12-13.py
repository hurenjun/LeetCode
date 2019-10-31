# -*- coding: UTF-8 -*-
# 12. Integer to Roman
# 13. Roman to Integer
# Renjun Hu, 3/13/2018

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        c = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '-', '-']
        digits = []
        result = []
        while num > 0:
            digits.append(num % 10)
            num /= 10
        for idx, d in enumerate(digits):
            ch_1, ch_5, ch_10 = c[idx*2], c[idx*2+1], c[idx*2+2]
            if 1 <= d <= 3:
                result = [ch_1]*d + result
            elif d == 4:
                result = [ch_1, ch_5] + result
            elif 5 <= d <= 8:
                result = [ch_5] + [ch_1]*(d-5) + result
            elif d == 9:
                result =  [ch_1, ch_10] + result
        return ''.join(result)
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char2num = {'I': 1, 'V': 5, 'IV': 4, 'IX': 9,
                    'X': 10, 'L': 50, 'XL': 40, 'XC': 90, 
                    'C': 100, 'D': 500, 'CD': 400, 'CM': 900,
                    'M': 1000}
        total = 0
        for ch in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:  # verify first, only occur once at most
            if ch in s:
                total += char2num[ch]
                s = s.replace(ch, '')
        for ch in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            total += char2num[ch] * s.count(ch)
            s = s.replace(ch, '')
        return total

    
s = Solution()

print s.romanToInt("LVIII")
print s.romanToInt("MCMXCIV")
