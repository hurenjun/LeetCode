class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x # guarantee l**2 <= x
        while l + 1 < r:
            m = (l + r) // 2
            if m**2 <= x:
                l = m
            else:
                r = m - 1
        if r**2 <= x:
            return r
        else:
            return l
    
s = Solution()
answer = s.mySqrt(101)  
print(answer)