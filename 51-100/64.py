class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        f = [[0] * n for _ in range(m)]
        for j in range(n):
            f[0][j] = grid[0][j] if j == 0 else f[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    f[i][j] = f[i-1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        return f[-1][-1]
        
    
s = Solution()
m = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
answer = s.minPathSum(m)  
print(answer) 