class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def subcheck(x, y):
            if x == y:
                return True
            else:
                lsx, lsy = [ch for ch in x], [ch for ch in y]
                lsx.sort()
                lsy.sort()
                if ''.join(lsx) != ''.join(lsy):
                    return False
                else:
                    for p in range(1, len(x), 1):
                        if subcheck(x[:p], y[:p]) and subcheck(x[p:], y[p:]):
                            return True
                        if subcheck(x[:p], y[len(y) - p:]) and subcheck(x[p:], y[:len(y) - p]):
                            return True
                    return False
            
        return subcheck(s1, s2)
    
            
s = Solution()
answer = s.isScramble('abcdefghijklmnopq', 'efghijklmnopqcadb')  
print(answer)