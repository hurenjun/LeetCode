class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l, r = -1, 0
        while r < len(nums) - 1:
            tmp = r
            for k in range(l + 1, r + 1):
                tmp = max(tmp, k + nums[k])
            if tmp == r:
                return False
            l, r = r, tmp
        return True
    
s = Solution()
answer = s.canJump([2,3,1,1,4])  
print(answer) 