class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        answer = defaultdict(list)
        for s in strs:
            char = [ch for ch in s]
            char.sort()
            answer[''.join(char)].append(s)
        return [x for x in answer.values()]
    
s = Solution()
answer = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])  
print(answer) 