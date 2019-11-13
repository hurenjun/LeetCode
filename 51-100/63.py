class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * n for _ in range(m)]
        for j in range(n):
            f[0][j] = 1 - obstacleGrid[0][j] if j == 0 else f[0][j-1] * (1 - obstacleGrid[0][j])
        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                    continue
                if j == 0:
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]
        
    
s = Solution()
m = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
answer = s.uniquePathsWithObstacles(m)  
print(answer) 