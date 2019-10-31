# -*- coding: UTF-8 -*-
# 9. Palindrome Number
# Renjun Hu, 3/1/2018

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        isPal = True
        for i in range(len(s)/2):
            if s[i] != s[-1-i]:
                isPal = False
                break
        return isPal    
        

s = Solution()
print s.isPalindrome(12)