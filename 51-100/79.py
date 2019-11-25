class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        n, m = len(board), len(board[0])
        self.walked = [[False] * m for _ in range(n)]
        self.answer = False
        self.offset = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(k, x, y):
            if k == len(word):
                self.answer = True
                return
            for ox, oy in self.offset:
                if 0 <= x + ox < n and 0 <= y + oy < m and not self.walked[x+ox][y+oy] and board[x+ox][y+oy] == word[k]:
                    self.walked[x+ox][y+oy] = True
                    dfs(k + 1, x+ox, y+oy)
                    self.walked[x+ox][y+oy] = False
                    if self.answer:
                        return
            return
        
        for x in range(0, n):
            for y in range(0, m):
                if board[x][y] == word[0]:
                    self.walked[x][y] = True
                    dfs(1, x, y)
                    self.walked[x][y] = False
        return self.answer
        
            
s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
answer = s.exist(board, 'ABCB')  
print(answer)