class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [0]
        base = 1
        for i in range(n):
            answer = answer + [base + x for x in answer[::-1]]
            base *= 2
        return answer
    
            
s = Solution()
answer = s.grayCode(3)  
print(answer)
