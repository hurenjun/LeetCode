class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last, tmp = 0, 0
        for ch in s:
            if ch == ' ':
                if tmp > 0:
                    last = tmp
                tmp = 0
            else:
                tmp += 1
        return tmp if tmp > 0 else last
    
s = Solution()
answer = s.lengthOfLastWord("   ")  
print(answer) 