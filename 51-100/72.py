class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1) + 1, len(word2) + 1
        f = [[i for i in range(m)]] + [[-1] * m for _ in range(n-1)]
        for i in range(0, n):
            f[i][0] = i
        for i in range(1, n):
            for j in range(1, m):
                # match
                if word1[i - 1] == word2[j - 1] and f[i-1][j-1] >= 0 and (f[i][j] == -1 or f[i-1][j-1] < f[i][j]):
                    f[i][j] = f[i-1][j-1]
                # replace
                if f[i-1][j-1] >= 0 and (f[i][j] == -1 or f[i-1][j-1] + 1 < f[i][j]):
                    f[i][j] = f[i-1][j-1] + 1
                # insert
                if f[i-1][j] >= 0 and (f[i][j] == -1 or f[i-1][j] + 1 < f[i][j]):
                    f[i][j] = f[i-1][j] + 1
                # delete
                if f[i][j-1] >= 0 and (f[i][j] == -1 or f[i][j-1] + 1 < f[i][j]):
                    f[i][j] = f[i][j-1] + 1
        print(f)
        return f[-1][-1]
        
s = Solution()
answer = s.minDistance('b', '')  
print(answer)