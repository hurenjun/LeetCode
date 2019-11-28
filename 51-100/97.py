class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        verified = set([0])
        for idx, ch in enumerate(s3):
            tmp = set()
            for l1 in verified:
                if l1 < len(s1) and s1[l1] == ch:
                    tmp.add(l1 + 1)
                if idx - l1 < len(s2) and s2[idx - l1] == ch:
                    tmp.add(l1)
            verified = tmp
        return len(s1) in verified
            
    
s = Solution()
answer = s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')  
print(answer)
