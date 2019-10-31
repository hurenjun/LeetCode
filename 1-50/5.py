# -*- coding: UTF-8 -*-
# 5. Longest Palindromic Substring
# Renjun Hu, 2/28/2018

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = "$#"
        for c in s:
            ss += '%s#' % c
        #print ss
        p = [0] * len(ss)
        mx, center, resLen, resCenter = 0, 0, 0, 0
        for idx in range(1, len(ss)):
            p[idx] = min(p[2*center-idx], mx-idx) if mx > idx else 1
            while idx+p[idx] < len(ss) and idx-p[idx] >= 0 and ss[idx+p[idx]] == ss[idx-p[idx]]:
                p[idx] += 1
            #print idx, p[idx]
            mx = max(mx, idx + p[idx])
            if resLen < p[idx]:
                resLen, resCenter = p[idx], idx
        #print resLen, resCenter
        return s[(resCenter-resLen)/2:(resCenter-resLen)/2+resLen-1]
            
    
    def longestPalindrome_v2(self, s):
        """
        :type s: str
        :rtype: str
        """
        best_len, x, y = 0, -1, -1
        for m in range(0, len(s)):
            for k in range(0, len(s)+1):
                if m-k >= 0 and m+k < len(s) and s[m-k] == s[m+k]:
                    continue
                else:
                    k = k - 1
                    if 2 * k + 1 > best_len:
                        x, y = m - k, m + k
                        best_len = y - x + 1
                    break
            for k in range(1, len(s)+1):
                if m-k+1 >= 0 and m+k < len(s) and s[m-k+1] == s[m+k]:
                    continue
                else:
                    k = k - 1
                    if k * 2 > best_len:
                        x, y = m - k + 1, m + k
                        best_len = y - x + 1
                    break
        return s[x:y+1]

s = Solution()
print s.longestPalindrome("a")
print s.longestPalindrome("aa")
print s.longestPalindrome("babad")
