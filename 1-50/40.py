class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import Counter
        candidates = Counter(candidates)
        comb = [[] for _ in range(target + 1)]
        for candidate, freq in candidates.items():
            for c in range(1, freq + 1):
                ls_app = [candidate] * c
                for exist in range(target - sum(ls_app), -1, -1):
                    if exist == 0:
                        comb[sum(ls_app)].append(ls_app)
                    else:
                        for ls_exist in comb[exist]:
                            if not candidate in ls_exist:
                                comb[exist + sum(ls_app)].append(ls_exist + ls_app)
        return comb[-1]
        
        
s = Solution()
answer = s.combinationSum2([10,1,2,7,6,1,5], 8)  
print(answer)