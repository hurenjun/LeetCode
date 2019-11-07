class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import math
        
        def times10(x):
            x2 = x + x
            x4 = x2 + x2
            return x4 + x4 + x2
        
        if dividend >= 0 and divisor > 0 or dividend < 0 and divisor< 0:
            isPos = True
        else:
            isPos = False
        dividend, divisor = abs(dividend), abs(divisor)
        answer, rest = 0, 0
        for ch in str(dividend):
            rest = times10(rest) + int(ch)
            answer = times10(answer)
            while rest >= divisor:
                answer += 1
                rest -= divisor
        if not isPos:
            answer = 0 - answer
        if answer >= math.pow(2, 31):
            answer = int(math.pow(2, 31)) - 1
        return answer


s = Solution()
answer = s.divide(7, -3)
print(answer)