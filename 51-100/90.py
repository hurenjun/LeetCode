class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        c = Counter(nums)
        nums = list(c.items())
        answer = []
        used = [0] * len(nums)
        while True:
            now = []
            for idx, n in enumerate(used):
                if n > 0:
                    now += [nums[idx][0]] * n
            answer.append(now)
            i = len(nums) - 1
            while i >= 0:
                if used[i] == nums[i][1]:
                    i -= 1
                else:
                    break
            if i == -1:
                break
            else:
                used[i] += 1
                for j in range(i + 1, len(nums)):
                    used[j] = 0
        return answer
        
        
    
            
s = Solution()
answer = s.subsetsWithDup([1,2,3])  
print(answer)
