class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        answer = [[0] * n for _ in range(n)]
        
        def valid(x, y):
            if 0 <= x < n and 0 <= y < n and answer[x][y] == 0:
                return True
            return False
        
        x, y, direction = 0, 0, 0
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for k in range(1, n**2 + 1):
            answer[x][y] = k
            if valid(x + delta[direction][0], y + delta[direction][1]):
                x, y = x + delta[direction][0], y + delta[direction][1]
            else:
                direction = (direction + 1) % 4
                x, y = x + delta[direction][0], y + delta[direction][1]
        return answer
    
s = Solution()
answer = s.generateMatrix(4)  
print(answer) 