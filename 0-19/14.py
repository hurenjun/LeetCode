# -*- coding: UTF-8 -*-
# 14. Longest Common Prefix
# 15. 3Sum
# 16. 3Sum Closest
# Renjun Hu, 4/3/2018

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """  
        if not strs:
            return ""
        for idx in range(len(strs[0])):
            ch = strs[0][idx]
            for str in strs:
                if idx == len(str):
                    return str
                if str[idx] != ch:
                    return strs[0][:idx]
        return strs[0]
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        nums.sort()
        triplets = []
        if len(nums) < 3:
            return triplets
        num_occ = defaultdict(int)
        for num in nums:
            num_occ[num] += 1
        for i in range(0, len(nums) - 2):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            num_occ[a] -= 1
            for j in range(i + 1, len(nums) - 1):
                b = nums[j]
                if a + b * 2 > 0:
                    break
                if j > i + 1 and b == nums[j - 1]:
                    continue
                num_occ[b] -= 1
                c = - (a + b)
                if num_occ[c] > 0 and c >= b:
                    triplets.append([a, b, c])
                num_occ[b] += 1
            num_occ[a] += 1
        return triplets
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        
s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4, -1])