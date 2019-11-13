class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer = []
        
        def dfs(k, col):
            if k == n:
                board = []
                for c in col:
                    row = ['.'] * n
                    row[c] = 'Q'
                    board.append(''.join(row))
                answer.append(board)
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
        return answer
    
s = Solution()
answer = s.solveNQueens(4)  
print(answer) 
