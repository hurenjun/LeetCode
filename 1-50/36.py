class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isUnique(ls):
            arr = [1] * 10
            for x in ls:
                if x != '.':
                    arr[int(x)] -= 1
            return all([x >=0 for x in arr])
        
        for row in range(9):
            if not isUnique(board[row]):
                return False
        for col in range(9):
            if not isUnique([boardRow[col] for boardRow in board]):
                return False
        for row in range(3):
            for col in range(3):
                if not isUnique([boardRow[c] for c in range(col * 3, col * 3 + 3) for boardRow in board[row*3:row*3+3]]):
                    return False
        return True
        
s = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
answer = s.isValidSudoku(board)  
print(answer)