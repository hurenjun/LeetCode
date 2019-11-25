class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        valid, now = -1 , 0
        while now < len(nums):
            valid += 1
            nums[valid] = nums[now]
            occ = 0
            while now < len(nums) and nums[now] == nums[valid]:
                occ += 1
                now += 1
                if occ == 2:
                    valid += 1
                    nums[valid] = nums[valid - 1]
        print(nums)
        return valid + 1
        
            
s = Solution()
answer = s.removeDuplicates([0,0,1,1,1,1,2,3,3])  
print(answer)