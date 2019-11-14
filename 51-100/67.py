class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b, c = a[::-1], b[::-1], []
        tmp = 0
        for k in range(max(len(a), len(b))):
            if k < len(a):
                tmp += int(a[k])
            if k < len(b):
                tmp += int(b[k])
            c.append(str(tmp % 2))
            if tmp >= 2:
                tmp = 1
            else:
                tmp = 0
        if tmp > 0:
            c.append(str(tmp))
        return ''.join(c[::-1])