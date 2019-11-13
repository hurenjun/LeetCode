class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[1] * n] + [[0] * n for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]
        
    
s = Solution()
answer = s.uniquePaths(100,100)  
print(answer) 