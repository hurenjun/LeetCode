class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer = []
        
        def dfs(k, col):
            if k == n:
                answer.append(1)
                return
            for i in range(n):
                # verify if i is a valid position for the queen in the k-th row
                isGood = True
                for j in range(0, k):
                    if col[j] == i:
                        isGood = False
                        break
                    if col[j] - i == k - j or col[j] - i == j - k:
                        isGood = False
                        break
                if isGood:
                    dfs(k + 1, col + [i])
            return
        
        dfs(0, [])
        return len(answer)
    
	def totalNQueensBit(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def queen(col, ld, rd):
            #check if all the column was filled by a queen.
            if col != filled:
                # valid positons 
                print(bin(col), bin(ld), bin(rd))
                pos = filled & ~(col|ld|rd)
                while pos:
                    index = pos & (~pos + 1) #try the rightmost one
                    pos -= index             #make this one invalid
                    queen(col|index, (ld|index) << 1, (rd|index) >> 1)    #find next one
            else:
                self.total += 1
        self.total, filled = 0, (1<<n)-1
        queen(0,0,0)
        return self.total
		
s = Solution()
for k in range(1, 10):
    answer = s.totalNQueens(k)  
    print(k, answer) 