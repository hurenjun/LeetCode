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
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        one_to_right = [[0] * m for _ in range(n)]
        for i in range(n):
            one_to_right[i][m - 1] = 1 if matrix[i][m - 1] == '1' else 0
            for j in range(m - 2, -1, -1):
                one_to_right[i][j] = one_to_right[i][j + 1] + 1 if matrix[i][j] == '1' else 0
        answer = 0
        for j in range(m):
            answer = max(answer, self.largestRectangleArea([one_to_right[i][j] for i in range(n)]))
        return answer
        
            
s = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
answer = s.maximalRectangle(matrix)  
print(answer)