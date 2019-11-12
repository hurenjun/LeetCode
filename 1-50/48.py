class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        cx, cy = (n - 1) * 0.5, (n - 1) * 0.5  # center
        step = 0
        for x in range((n + 1) // 2):
            for y in range(x, n - x - 1):
                nx, ny = x, y  # now
                prev = matrix[x][y]
                while True:
                    dx, dy = cx - nx, cy - ny  # difference
                    dx, dy = -dy, dx  # rotate
                    tx, ty = int(cx + dx), int(cy + dy) # to
                    matrix[tx][ty], prev = prev, matrix[tx][ty]
                    nx, ny = tx, ty
                    if tx == x and ty == y:
                        break
        return
    
s = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
answer = s.rotate(matrix)  
print(answer) 