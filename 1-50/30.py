class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return []
        length = len(words[0])
        words.sort()
        sketch = [0] * 26
        for word in words:
            for ch in word:
                sketch[ord(ch) - ord('a')] += 1
        answer = []
        comp = [0] * 26
        for k in range(len(words) * length - 1):
            comp[ord(s[k]) - ord('a')] += 1
        for i in range(len(s)):
            j = i + len(words) * length
            if j > len(s):
                break
            comp[ord(s[j - 1]) - ord('a')] += 1
            if all([sketch[z] == comp[z] for z in range(26)]):
                # check
                slices = [s[k:k+length] for k in range(i, j, length)]
                slices.sort()
                if all([slices[z] == words[z] for z in range(len(words))]):
                    answer.append(i)
            comp[ord(s[i]) - ord('a')] -= 1
            
        return answer

s = Solution()
answer = s.findSubstring("a", [])
print(answer)