class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.answer = []
        def dfs(k, ss, nums):
            if k == 4:
                if 0 <= int(ss) <= 255 and str(int(ss)) == ss:
                    nums.append(ss)
                    self.answer.append('.'.join(nums))
                return
            for d in range(1, 4):
                if d >= len(ss):
                    break
                if int(ss[:d]) <= 255 and str(int(ss[:d])) == ss[:d]:
                    dfs(k + 1, ss[d:], nums + [ss[:d]])
            return
        dfs(1, s, [])
        return self.answer
        
    
s = Solution()
answer = s.restoreIpAddresses('010010')  
print(answer)
