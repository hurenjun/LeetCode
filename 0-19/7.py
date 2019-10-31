# -*- coding: UTF-8 -*-
# 7. Reverse Integer
# Renjun Hu, 3/1/2018

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        x = abs(x)
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10
        y = y * sign
        if -2**31 <= y <= 2**31 - 1:
            return y
        else:
            return 0
        