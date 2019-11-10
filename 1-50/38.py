class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            ss = ''
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[i] == s[j]:
                    j += 1
                ss += '%d%s' % (j - i, s[i])
                i = j
            s = ss
        return s
        
s = Solution()
answer = s.countAndSay(6)  
print(answer)