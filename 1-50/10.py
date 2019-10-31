# -*- coding: UTF-8 -*-
# 10. Regular Expression Matching
# Renjun Hu, 3/2/2018

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        while '**' in p:  # remove duplicated *
            p = p.replace('**', '*')
        s, p = s + '#', p + '#'
        import numpy as np
        match = np.zeros((len(p)+1, len(s)+1), dtype=np.int32)
        match[0][0] = 1
        for i, cp in enumerate(p):
            for j, cs in enumerate(s):
                if not match[i][j]:
                    continue
                if cp == '.' or cp == cs:
                    match[i+1][j+1] = 1
                if i + 1 < len(p) and p[i+1] == '*':
                    match[i+2][j] = 1
                    if cp == '.':
                        match[i+2][j+1:] = 1
                    else:
                        for k in range(j, len(s)):
                            if s[k] == cp:
                                match[i+2][k+1] = 1
                            else:
                                break
        return True if match[len(p)][len(s)] == 1 else False
    
    
s = Solution()
print s.isMatch("", "c*")
#print s.isMatch("aa", "a*")
#print s.isMatch("ab", ".*")
#print s.isMatch("aab", "c*a*b")
#print s.isMatch("mississippi", "mis*is*p*.")