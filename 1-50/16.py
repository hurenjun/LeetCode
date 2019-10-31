class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        i = 0
        answer = float('inf')
        
        while i < n - 2:
            j = i + 1
            k = n - 1

            while j < k :
                sum_ = nums[i] + nums[j] + nums[k]

                
                if abs(answer - target) > abs(sum_ - target):
                    answer = sum_
                
                if sum_ < target:
                    j += 1
                    
                elif sum_ > target:
                    k -= 1
                else :
                    return target
            i += 1
            
        return answer