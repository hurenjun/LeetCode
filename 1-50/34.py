class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(l, r):
            while l <= r:
                m = (l + r) // 2
                x, y, z = nums[l], nums[m], nums[r]
                if target == y:
                    ls = [m]
                    if x == target:
                        ls.append(l)
                    else:
                        ls += dfs(l, m - 1)
                    if z == target:
                        ls.append(r)
                    else:
                        ls += dfs(m + 1, r)
                    return ls
                elif target < y:
                    r = m - 1
                else:
                    l = m + 1
            return []
        
        hit = dfs(0, len(nums) - 1)
        if not hit:
            return [-1, -1]
        else:
            return [min(hit), max(hit)]
        
s = Solution()
answer = s.searchRange([8, 8, 8, 8, 8, 8, 8, 8, 10], 8)  
print(answer)