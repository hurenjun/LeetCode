class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        n = n * 2
        
        def dfs(tmp, k, remained_left):
            if k + remained_left > n:
                return
            if k + remained_left == n:
                answer.append(tmp + ')' * remained_left)
                return
            if remained_left > 0:
                dfs(tmp + ')', k + 1, remained_left - 1)
            dfs(tmp + '(', k + 1, remained_left + 1)
            return
        
        if n > 0:
            dfs('', 0, 0)
        return answer
    
s = Solution()
answer = s.generateParenthesis(2)
print(answer)