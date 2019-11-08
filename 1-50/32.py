class Solution(object):
    def longestValidParenthesesDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        answer = 0
        f = [0] * (length + 1)
        for i in range(2, length + 1):
            if s[i - 2] == '(' and s[i - 1] == ')':
                f[i] = f[i - 2] + 2
            elif s[i - 2] == ')' and s[i - 1] == ')' and i - f[i - 1] - 2 >= 0 and s[i - f[i - 1] - 2] == '(':
                f[i] = f[i - 1] + 2 + f[i - f[i - 1] - 2]
            answer = max(answer, f[i])
        return answer   
    
    def longestValidParenthesesStack(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        ls = [-1]
        answer = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                ls.append(idx)
            else:
                if not ls:
                    ls.append(idx)
                else:
                    l = ls.pop()
                    if not ls:
                        ls.append(idx)
                    else:
                        answer = max(answer, idx - ls[-1])
        return answer
                
                

s = Solution()
answer = s.longestValidParentheses(')(((((()())()()))()(()))(')  # ')()())'
print(answer)