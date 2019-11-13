class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        answer = ''
        digits = [x + 1 for x in range(n)]
        groupSize = 1
        for i in range(1, n + 1):
            groupSize *= i
        for i in range(n, 0, -1):
            groupSize = groupSize // i
            x, k = k // groupSize, k % groupSize
            answer += str(digits[x])
            del digits[x]
        return answer
    
s = Solution()
answer = s.getPermutation(4,2)  
print(answer) 