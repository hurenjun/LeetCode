class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for x in path:
            if not x or x == '.':
                continue
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/' + '/'.join(stack)
    
s = Solution()
answer = s.simplifyPath('/a//b////c/d//././/..')  
print(answer)