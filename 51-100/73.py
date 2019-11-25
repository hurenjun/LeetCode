class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return None
        
        n, m = len(matrix), len(matrix[0])
        
        def cleanRow(row):
            for k in range(m):
                matrix[row][k] = 0
                
        def cleanColumn(col):
            for k in range(n):
                matrix[k][col] = 0
                
        zeroRowOne, zeroColOne = False, False
        for k in range(m):
            if matrix[0][k] == 0:
                zeroRowOne = True
                break
        for k in range(n):
            if matrix[k][0] == 0:
                zeroColOne = True
                break
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        for k in range(1, m):
            if matrix[0][k] == 0:
                cleanColumn(k)
        for k in range(1, n):
            if matrix[k][0] == 0:
                cleanRow(k)
        if zeroRowOne:
            cleanRow(0)
        if zeroColOne:
            cleanColumn(0)
        
        for row in matrix:
            print(row)
        return None
        
            
s = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
answer = s.setZeroes(matrix)  
print(answer)