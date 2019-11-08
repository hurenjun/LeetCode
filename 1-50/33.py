class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            x, y, z = nums[l], nums[m], nums[r]
            if target == y:
                return m
            if x <= y:
                if x <= target <= y:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if y <= target <= z:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        
                
                

s = Solution()
answer = s.search([8, 1, 2, 3, 4, 5, 6, 7], 6)  # ')()())'
print(answer)