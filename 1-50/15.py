class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        c = Counter(nums)
        arr = list(c.items())
        arr.sort(key=lambda x: x[0])
        answer = []
        for idx, (x, fx) in enumerate(arr):
            for y, fy in arr[idx:]:
                z = -x - y
                if y <= z and z in c:
                    c[x] -= 1
                    c[y] -= 1
                    c[z] -= 1
                    if c[x] >= 0 and c[y] >= 0 and c[z] >= 0:
                        answer.append([x, y, z])
                    c[x] += 1
                    c[y] += 1
                    c[z] += 1
                if z < y:
                    break
        return answer