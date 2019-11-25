class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        area_to_right, area_to_left = [0] * len(heights), [0] * len(heights)
        stack = [(-1, 0)]  # (index, height)
        for idx, height in enumerate(heights + [0]):
            while height < stack[-1][1]:
                l, h = stack.pop()
                area_to_right[l] = (idx - l) * h
            stack.append((idx, height))
        stack = [(-1, 0)]
        for idx, height in enumerate(heights[::-1] + [0]):
            while height < stack[-1][1]:
                l, h = stack.pop()
                area_to_left[len(heights) - 1 - l] = (idx - l) * h
            stack.append((idx, height))
        answer = [area_to_right[i] + area_to_left[i] -heights[i] for i in range(len(heights))]
        return max(answer)
        
            
s = Solution()
answer = s.largestRectangleArea([2,1,5,6,2,3])  
print(answer)