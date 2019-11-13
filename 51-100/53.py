class Solution(object):
    def maxSubArrayLinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer, tmp = nums[0], 0
        l, r = 0, 0
        while r < len(nums):
            tmp += nums[r]
            answer = max(answer, tmp)
            r += 1
            if tmp < 0:
                tmp, l = 0, r
        return answer
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.answer = nums[0]
        
        def divide_and_conquer(k):
            if k == 0:
                return nums[0]
            tmp = divide_and_conquer(k - 1)
            self.answer = max(self.answer, tmp)
            return max(tmp + nums[k], nums[k])
        
        x = divide_and_conquer(len(nums) - 1)
        return max(x, self.answer)
    
    
s = Solution()
answer = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])  
print(answer) 