class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def createAux(w):
            aux = [0] * len(w)  # aux[i] is the maximum length s.t. prefix == suffix
            i, m = 1, 0  # w[0, m] = w[, i], excluding m & i
            while i < len(w):
                if w[m] == w[i]:
                    m += 1
                    aux[i] = m
                    i += 1
                elif m > 0:
                    m = aux[m - 1]
                else:
                    aux[i] = m
                    i += 1
            return aux
        
        if len(needle) == 0:
            return 0
        aux = createAux(needle)
        i, j = 0, 0
        while j < len(haystack):
            if needle[i] != haystack[j]:
                if i == 0:
                    j += 1
                else:
                    i = aux[i - 1]
            else:
                i += 1
                j += 1
                if i == len(needle):
                    return j - i
        return -1
        

s = Solution()
answer = s.strStr('acfacabacabacacdk', 'acabacacd')
print(answer)