class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        if not height:
            return answer
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < left_max:
                    answer += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if height[r] < right_max:
                    answer += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1
        return answer
        
        
s = Solution()
answer = s.trap([0,5,2,0,6,1,0,3,0,1])  
print(answer) 