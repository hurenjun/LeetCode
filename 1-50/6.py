# -*- coding: UTF-8 -*-
# ZigZag Conversion
# Renjun Hu, 2/28/2018

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        for _ in range(numRows):
            result.append([])
        x, y, state = 0, 0, 0
        for c in s:
            if state == 0:
                result[x].append(c)
                x += 1
                if x == numRows:
                    x, y, state = x - 2 if x - 2 >= 0 else 0, y + 1, 1
            else:
                result[x].append(c)
                x, y = x - 1, y + 1
                if x == -1:
                    x, y, state = x + 2 if x + 2 < numRows else 0, y - 1, 0
        zigzag = ''
        for ls in result:
            zigzag += ''.join(ls)
        return zigzag
    
    def convert_v2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ''
        for i in range(min(numRows, len(s))):
            skip = [2 * (numRows - 1 - i), 2 * i]
            if 0 in skip:
                skip.remove(0) 
            pos = i
            zigzag += s[pos]
            for j in range(len(s)):
                pos += skip[j%len(skip)]
                if pos < len(s):
                    zigzag += s[pos]
                else:
                    break
        return zigzag
                

s = Solution()
print s.convert("PAYPALISHIRING", 1)
print s.convert("PAYPALISHIRING", 4)
