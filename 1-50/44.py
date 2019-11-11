class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = [0]
        for ch in p:
            if ch == '?':
                match = [x + 1 for x in match if x < len(s)]
            elif ch == '*':
                if len(match) > 0:
                    match = [x for x in range(min(match), len(s) + 1)]
            else:
                match = [x + 1 for x in match if x < len(s) and s[x] == ch]
            #print(ch, match)
        return len(s) in match

s = Solution()
answer = s.isMatch('aa', 'a')  
print(answer) 