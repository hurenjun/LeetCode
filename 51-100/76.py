class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(list(t))
        l, r, remained = 0, 0, len(t)
        answer = None
        while r < len(s):
            while r < len(s):
                if s[r] in c:
                    c[s[r]] -= 1
                    if c[s[r]] >= 0:
                        remained -= 1
                    if remained == 0:
                        r += 1
                        break
                r += 1
            if remained == 0:
                while l < r:
                    if s[l] in c:
                        c[s[l]] += 1
                        if c[s[l]] > 0:
                            remained += 1
                            break
                    l += 1
                if answer is None or r - l < answer[1]- answer[0]:
                    answer = [l, r]
                l += 1
        
        if answer is None:
            return ''
        else:
            return s[answer[0]:answer[1]]

            
s = Solution()
answer = s.minWindow('ADOBECODEBANC', 'ABC')  
print(answer)