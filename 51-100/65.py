class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def validDisit(s):
            if len(s) == 0:
                return False
            if s[0] == '+' or s[0] == '-':
                start = 1
            else:
                start = 0
            if sum([1 if x == '.' else 0 for x in s[start:]]) > 1:
                return False
            if sum([1 if '0' <= x <= '9' else 0 for x in s[start:]]) == 0:
                return False
            return all(['0' <= x <= '9' or x == '.' for x in s[start:]])
        
        def validInt(s):
            if s is None:
                return True
            if len(s) == 0:
                return False
            if s[0] == '+' or s[0] == '-':
                start = 1
            else:
                start = 0
            if sum([1 if '0' <= x <= '9' else 0 for x in s[start:]]) == 0:
                return False
            return all(['0' <= x <= '9' for x in s[start:]])
        
        s = s.strip()
        if len(s) == 0:
            return False
        if 'e' in s:
            tmp = s.split('e')
            if len(tmp) > 2:
                return False
            s, ss = tmp[0], tmp[1]
        else:
            ss = None
        
        return validDisit(s) and validInt(ss)
		
    
s = Solution()
answer = s.isNumber('.03 ')  
print(answer) 