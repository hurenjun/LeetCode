class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def valid(x, y):
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not matrix[x][y] is None:
                return True
            else:
                return False
        
        answer = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return answer
        
        x, y, direction = 0, 0, 0
        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while len(answer) < len(matrix) * (len(matrix[0])):
            answer.append(matrix[x][y])
            matrix[x][y] = None
            if valid(x + delta[direction][0], y + delta[direction][1]):
                x, y = x + delta[direction][0], y + delta[direction][1]
            else:
                direction = (direction + 1) % 4
                x, y = x + delta[direction][0], y + delta[direction][1]
        return answer