class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = [list(nums)]
        if len(nums) < 2:
            return answer
        while True:
            i = len(nums) - 1
            while i > 0 and nums[i - 1] >= nums[i]:
                i -= 1
            if i == 0:
                break
            j = -1
            for k in range(i, len(nums)):
                if nums[k] > nums[i - 1] and (j == -1 or nums[k] < nums[j]):
                    j = k
            tmp = nums[i - 1]
            nums[i - 1] = nums[j]
            nums[j] = tmp
            tmp = nums[i:]
            tmp.sort()
            nums = nums[:i] + tmp
            answer.append(list(nums))
        return answer

s = Solution()
answer = s.permute([1,2,2,1,1])  
print(answer) 
print(len(answer))