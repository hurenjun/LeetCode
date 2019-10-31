# -*- coding: UTF-8 -*-
# 11. Container With Most Water
# Renjun Hu, 3/2/2018

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l, r = 0, len(height)-1
        while l < r:
            if (r-l) * min(height[l], height[r]) > area:
                area = (r-l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
    
    def maxArea_v1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = [(1, height[0])], [(len(height), height[-1])]
        x = height[0]
        for i in range(1, len(height)):
            if height[i] > x:
                x = height[i]
                l.append((i+1, x))
        x = height[-1]
        for i in range(len(height)-2, -1, -1):
            if height[i] > x:
                x = height[i]
                r.append((i+1, x))
        area = 0
        for lx in l:
            for rx in r:
                if rx[0] <= lx[0]:
                    break
                if (rx[0] - lx[0]) * min(lx[1], rx[1]) > area:
                    area = (rx[0] - lx[0]) * min(lx[1], rx[1])
        return area
        
    
s = Solution()
print s.maxArea([1,8,6,2,5,4,8,3,7])
