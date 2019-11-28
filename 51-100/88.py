class Solution(object):
    def mergev1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        upbound = max(nums1[m - 1], nums2[n - 1]) + 1
        i, j, jmax, k = 0, 0, -1, 0
        while k < n:
            x = nums1[i] if i < m else upbound
            y = nums2[j] if j <= jmax else upbound
            z = nums2[k]
            #print(x, y, z)
            if x <= y and x <= z:
                i += 1
            elif z <= x and z <= y:
                nums1[i] = z
                if j > jmax:
                    j, jmax = 0, -1
                if x != upbound:
                    jmax += 1
                    nums2[jmax] = x
                i, k = i + 1, k + 1
            else:
                nums1[i] = y
                i, j = i + 1, j + 1
                if j > jmax:
                    j, jmax = 0, -1
                if x != upbound:
                    if jmax + 1 == k:
                        for jj in range(j, jmax+1):
                            nums2[jj-j] = nums2[jj]
                        j, jmax = 0, jmax - j
                    jmax += 1
                    nums2[jmax] = x
            #print(nums1[:i], nums1[i:], nums2[0:jmax+1], nums2[k:], i, j, jmax, k)
        if j <= jmax:
            for ii in range(m - 1, i - 1, -1):
                nums1[ii + jmax - j + 1] = nums1[ii]
            while j <= jmax:
                nums1[i] = nums2[j]
                i, j = i + 1, j + 1
        #print(nums1[:n+m])
        return
        
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i, j, k = m - 1, n - 1, n + m - 1
        lowerbound = min(nums1[0], nums2[0]) - 1
        while i >= 0 or j >= 0:
            x = nums1[i] if i >= 0 else lowerbound
            y = nums2[j] if j >= 0 else lowerbound
            if x >= y:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        print(nums1[:n+m])
        return
                
    
            
s = Solution()
answer = s.merge([-1,0,1,1,0,0,0,0,0], 4, [-1,0,2,2,3], 5)  
print(answer)
