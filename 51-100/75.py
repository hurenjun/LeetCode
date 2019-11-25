class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return None
        l, r = -1, n
        x= 0
        while x < r:
            if nums[x] == 0:
                l += 1
                nums[x], nums[l] = nums[l], nums[x]
            elif nums[x] == 2:
                r -= 1
                nums[x], nums[r] = nums[r], nums[x]
                continue
            x += 1
            #print(l, x, r, nums)
        #print(nums)
        return None
        

            
s = Solution()
answer = s.sortColors([2,0,2,1,1,0])  
print(answer)