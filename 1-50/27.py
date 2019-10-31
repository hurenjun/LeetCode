class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_pos = 0
        for idx, num in enumerate(nums):
            if num != val:
                nums[write_pos] = num
                write_pos += 1
        return write_pos
    

s = Solution()
nums = [0,1,2,2,3,0,4,2]
answer = s.removeElement(nums, 0)
print(answer)
print(nums[:answer])