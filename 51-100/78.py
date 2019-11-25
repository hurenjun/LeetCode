class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.answer = []
        
        def dfs(ls, k):
            self.answer.append(ls)
            for i in range(k, len(nums)):
                dfs(ls + [nums[i]], i + 1)
            return
        
        dfs([], 0)
        return self.answer
            
s = Solution()
answer = s.subsets([1, 2, 3, 4])  
print(answer)