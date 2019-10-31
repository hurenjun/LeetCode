# -*- coding: UTF-8 -*-
# 4. Median of Two Sorted Arrays
# Renjun Hu, 2/27/2018

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import sys
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, m, nums2, n = nums2, n, nums1, m
        if m == 0:
            return nums2[n/2] if n %2 == 1 else .5 * (nums2[n/2]+nums2[n/2-1])
        if n + m == 2:
            return .5 * (nums1[0] + nums2[0])
        l, r = 0, m
        while l <= r:
            pos1 = (l + r) / 2  # splitting position of nums1, [:pos1] in left and [pos1:] in right 
            pos2 = (n + m) / 2 - pos1  # splitting position of nums2
            # check if the splitting is corrct
            left1 = nums1[pos1-1] if pos1-1 >= 0 else -sys.maxint
            left2 = nums2[pos2-1] if pos2-1 >= 0 else -sys.maxint
            right1 = nums1[pos1] if pos1 < m else sys.maxint
            right2 = nums2[pos2] if pos2 < n else sys.maxint
            if max(left1, left2) <= min(right1, right2):
                if (n + m) % 2 == 0:
                    return .5 * (max(left1, left2) + min(right1, right2))
                else:
                    return float(min(right1, right2))
            elif left1 > right2:
                r = pos1 - 1
            elif left2 > right1:
                l = pos1 + 1
            else:
                print 'no move'
                print nums1[pos1-1:pos2+1]
                print nums2[pos2-1, pos2+1]
                return None
    

s = Solution()
print s.findMedianSortedArrays([10], [1, 3, 5, 7, 9])
print s.findMedianSortedArrays([0], [1, 3, 5, 7, 9])          
            
        
    