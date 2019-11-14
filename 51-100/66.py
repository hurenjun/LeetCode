class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                tmp = 0
                break
        if tmp == 0:
            return digits
        else:
            return [1] + digits
        
        
    
s = Solution()
answer = s.plusOne([9,9,9,9])  
print(answer) 