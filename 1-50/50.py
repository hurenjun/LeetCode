class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            negN = True
        else:
            negN = False
        nb2 = bin(n)[2:]
        answer, factor = 1., x
        for ch in nb2[::-1]:
            if ch == '1':
                answer *= factor
            factor *= factor
        if negN:
            answer = 1. / answer
        return answer
    
s = Solution()
answer = s.myPow(2.00000, -2)  
print(answer) 