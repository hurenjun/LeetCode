class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r, step = 0, 0, 0
        if len(nums) <= 1:
            return 0
        while True:
            tmp = -1
            for i in range(l, r + 1):
                tmp = max(tmp, i + nums[i])
            step += 1
            if len(nums) - 1 <= tmp:
                break
            l = r + 1
            r = tmp
            #print(l, r, step)
        return step

s = Solution()
answer = s.jump([2,3,1,1,4])  
print(answer) 