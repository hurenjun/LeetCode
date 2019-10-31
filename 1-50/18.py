class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        comb = defaultdict(list)
        for idx1, num1 in enumerate(nums):
            for idx2 in range(idx1 + 1, len(nums)):
                num2 = nums[idx2]
                comb[num1 + num2].append((idx1, idx2))
        answer = set()
        for k, v in comb.items():
            if target - k < k or not target - k in comb:
                continue
            for idx1, idx2 in v:
                for idx3, idx4 in comb[target - k]:
                    if idx3 != idx1 and idx3 != idx2 and idx4 != idx1 and idx4 != idx2:
                        tmp = [nums[idx1], nums[idx2], nums[idx3], nums[idx4]]
                        tmp.sort()
                        answer.add('\t'.join(map(str, tmp)))
        answer_ls = []
        for x in answer:
            y = [int(s) for s in x.split()]
            answer_ls.append(y)
        return answer_ls
            
                
            
        
s = Solution()
answer = s.fourSum([1, 0, -1, 0, -2, 2], 0)
print(answer)