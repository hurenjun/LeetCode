class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        changed = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[i] < nums[j]:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
                        changed = True
                        for k in range(i + 1, len(nums)):
                            for l in range(k + 1, len(nums)):
                                if nums[k] > nums[l]:
                                    tmp = nums[k]
                                    nums[k] = nums[l]
                                    nums[l] = tmp
                        break
            if changed:
                break
                
        if not changed:
            for i in range(len(nums) / 2):
                tmp = nums[i]
                nums[i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = tmp
        return None

s = Solution()
answer = s.nextPermutation([4,2,0,2,3,2,0])
print(answer)