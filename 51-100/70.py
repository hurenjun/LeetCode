class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        x, y = 1, 2
        for _ in range(3, n + 1):
            x, y = y, x + y
        return y
    
s = Solution()
answer = s.climbStairs(4)  
print(answer)