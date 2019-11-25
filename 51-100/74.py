class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = (l + r) // 2
            #print(l, r, mid, mid // m, mid % m)
            if matrix[mid // m][mid % m] == target:
                return True
            elif matrix[mid // m][mid % m] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

            
s = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
answer = s.searchMatrix(matrix, 13)  
print(answer)