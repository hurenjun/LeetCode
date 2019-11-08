class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target <= nums[0]:
            return 0
        l, r = 0, len(nums) - 1  # we ensure that nums[l] < target
        while l + 1 < r:
            m = (l + r) / 2
            x, y, z = nums[l], nums[m], nums[r]
            if y == target:
                return m
            elif target < y:
                r = m - 1
            else:
                l = m
        while l < len(nums) and nums[l] < target:
            l += 1
        return l
        
s = Solution()
answer = s.searchInsert([1, 2, 2, 5, 6], 3)  
print(answer)