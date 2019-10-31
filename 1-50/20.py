class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif ch == ')':
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if pop != '(':
                    return False
            elif ch == ']':
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if pop != '[':
                    return False
            elif ch == '}':
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if pop != '{':
                    return False
        if len(stack) > 0:
            return False
        return True
    
    
s = Solution()
answer = s.isValid('{[]}')
print(answer)