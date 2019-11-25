class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.answer = []
        
        def dfs(ls):
            if len(ls) == k:
                self.answer.append(ls)
                return
            start = 1 if not ls else ls[-1] + 1
            for i in range(start, n + len(ls) - k + 2):
                dfs(ls + [i])
            return
        
        dfs([])
        return self.answer

            
s = Solution()
answer = s.combine(4, 3)  
print(answer)