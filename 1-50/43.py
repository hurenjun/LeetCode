class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        answer = [0] * (len(num1) + len(num2))
        for i, chi in enumerate(num1):
            for j, chj in enumerate(num2):
                answer[i + j] += int(chi) * int(chj)
                if answer[i + j] > 9:
                    answer[i + j + 1] += answer[i + j] // 10
                    answer[i + j] = answer[i + j] % 10
        i = len(num1) + len(num2) - 1
        while i > 0 and answer[i] == 0:
            i -= 1
        answer = list(map(str, answer[0:i+1]))
        return ''.join(answer[::-1])
        

s = Solution()
answer = s.multiply('0', '0')  
print(answer) 