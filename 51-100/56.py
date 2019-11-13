class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = [x for x in intervals if x[0] <= x[1]]
        intervals.sort()
        answer = []
        l = 0
        while l < len(intervals):
            x, y = intervals[l]
            l += 1
            while l < len(intervals) and y >= intervals[l][0]:
                y = max(y, intervals[l][1])
                l += 1
            answer.append([x, y])
        return answer
    
s = Solution()
answer = s.merge([[1,4],[4,5]])  
print(answer) 