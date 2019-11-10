class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb = [[] for _ in range(target + 1)]
        for candidate in candidates:
            ls_app = []
            while True:
                ls_app.append(candidate)
                if sum(ls_app) > target:
                    break
                for exist in range(target - sum(ls_app) + 1):
                    if exist == 0:
                        comb[sum(ls_app)].append([] + ls_app)
                    else:
                        for ls_exist in comb[exist]:
                            if not candidate in ls_exist:
                                comb[exist + sum(ls_app)].append(ls_exist + ls_app)
                            else:
                                break
        return comb[-1]
        
        
s = Solution()
answer = s.combinationSum([2, 3, 5], 8)  
print(answer)