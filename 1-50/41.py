class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in range(len(nums)):
            if nums[idx] < 1 or nums[idx] > len(nums):
                nums[idx] = 0
        #print(nums)
        for idx in range(len(nums)):
            if nums[idx] % (len(nums) + 1) > 0:
                nums[nums[idx] % (len(nums) + 1) - 1] += len(nums) + 1
            #print(nums)
        for idx in range(len(nums)):
            if nums[idx] < len(nums) + 1:
                return idx + 1
        return len(nums) + 1
        
        
s = Solution()
answer = s.firstMissingPositive([3,-1,1,4])  
print(answer)