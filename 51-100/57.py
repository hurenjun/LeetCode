class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        less, last_overlap = -1, len(intervals)
        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                less = idx
            elif not(interval[1] < newInterval[0] or newInterval[1] < interval[0]): ##overlap
                last_overlap = idx
                newInterval[0], newInterval[1] = min(interval[0], newInterval[0]), max(interval[1], newInterval[1])
            elif interval[0] > newInterval[1]:
                break
        if last_overlap == len(intervals):
            return intervals[:less+1] + [newInterval] + intervals[less+1:]
        else:
            return intervals[:less+1] + [newInterval] + intervals[last_overlap+1:]
    
s = Solution()
answer = s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])  
print(answer) 