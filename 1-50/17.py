class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit2str = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        answers = []
        def dfs(k, ans):
            if k == len(digits):
                answers.append(ans)
                return
            for ch in digit2str[int(digits[k])]:
                dfs(k + 1, ans + ch)
        
        if len(digits) > 0:
            dfs(0, '')
        return answers
            
        
s = Solution()
answer = s.letterCombinations('23')
print(answer)