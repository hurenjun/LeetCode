class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def clear(valid, row, col, ch):
            hist = []
            for y in range(9):
                if valid[row][y] and valid[row][y][ch] == 1:
                    valid[row][y][ch] = 0
                    hist.append([row, y, ch])
            for x in range(9):
                if valid[x][col] and valid[x][col][ch] == 1:
                    valid[x][col][ch] = 0
                    hist.append([x, col, ch])
            for x in range(3):
                for y in range(3):
                    if valid[row // 3 * 3 + x][col // 3 * 3 + y] and valid[row // 3 * 3 + x][col // 3 * 3 + y][ch] == 1:
                        valid[row // 3 * 3 + x][col // 3 * 3 + y][ch] = 0
                        hist.append([row // 3 * 3 + x, col // 3 * 3 + y, ch])
            return hist
        
        def dfs(filled, dots, valid, clearHist):
            if filled == dots:
                return True
            minValid = 11
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.' and sum(valid[row][col]) < minValid:  # need to fill this cell
                        sx, sy, minValid = row, col, sum(valid[row][col])
            #print('select:', sx, sy, valid[sx][sy])
            if minValid == 11:
                return False
            for ch in [x for x in range(1, 10) if valid[sx][sy][x] > 0]:
                #print('fill:', sx, sy, ch, filled + 1, dots)
                board[sx][sy] = str(ch)
                clearHist.append(clear(valid, sx, sy, ch))
                if dfs(filled + 1, dots, valid, clearHist):
                    return True
                board[sx][sy] = '.'
                cleared = clearHist.pop()
                for item in cleared:
                    valid[item[0]][item[1]][item[2]] = 1
                #print('clear:', sx, sy, ch, cleared)
            return False
        
        valid = []
        for _ in range(9):
            valid.append([])
            for __ in range(9):
                valid[-1].append([1] * 10)
        dots = 0
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    del valid[row][col][:]  
                    clear(valid, row, col, int(board[row][col]))
                else:
                    dots += 1
        dfs(0, dots, valid, [])
        for row in board:
            print(row)
        return None
        
s = Solution()
board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]
answer = s.solveSudoku(board)  
print(answer)