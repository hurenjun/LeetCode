class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        chars = [ch for ch in s]
        x, y = 1, 1
        for i in range(1, len(chars)):
            if chars[i] == '0':
                if chars[i - 1] == '1' or chars[i - 1] == '2':
                    z = x
                else:
                    return 0
            elif chars[i - 1] == '0':
                z = y
            elif int(chars[i-1] + chars[i]) <= 26:
                z = x + y
            else:
                z = y
            x, y = y, z
        return y
        
        
    
            
s = Solution()
answer = s.numDecodings('01')  
print(answer)
