# -*- coding: UTF-8 -*-
# 8. String to Integer (atoi)
# Renjun Hu, 3/1/2018

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        valid, sign, y = False, 1, 0
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and (str[i] == '+' or str[i] == '-'):
            sign = 1 if str[i] == '+' else -1
            i += 1
        for c in str[i:]:
            if c >= '0' and c <= '9':
                y = y * 10 + int(c) - 0
                valid = True
                if y * sign > 2**31 - 1:
                    y = 2**31 - 1
                    break
                elif y * sign < -2**31:
                    y = 2**31
                    break
            else:
                break
        return y * sign if valid else 0

s = Solution()
print s.myAtoi("-91283472332")