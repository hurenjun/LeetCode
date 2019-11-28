class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        answer = [0] * (n + 1)
        answer[0] = answer[1] = 1
        for k in range(2, n + 1):
            for root in range(1, k + 1):
                answer[k] += answer[root - 1] * answer[k - root]
        return answer[-1]
        
    
s = Solution()
answer = s.numTrees(3)  
print(answer)
