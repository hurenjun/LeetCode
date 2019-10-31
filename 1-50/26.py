class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write_pos, prev = 0, None
        for idx, num in enumerate(nums):
            if prev is None or prev != num:
                prev = num
                nums[write_pos] = num
                write_pos += 1
        return write_pos
    

s = Solution()
answer = s.removeDuplicates([1, 1, 2])
print(answer)