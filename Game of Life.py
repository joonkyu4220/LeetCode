class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        numCol = len(board[0])
        def neighborCoord(i, j, numRow, numCol):
            default = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            for i in range(7, -1, -1):
                if default[i][0] == -1 or default[i][0] == numRow or default[i][1] == -1 or default[i][1] == numCol:
                    default = default[:i] + default[i+1:]
            return default
        for i in range(numRow):
            for j in range(numCol):
                neighbors = neighborCoord(i, j, numRow, numCol)
                for n in neighbors:
                    if board[n[0]][n[1]] % 2 == 1:
                        board[i][j] += 2
        for i in range(numRow):
            for j in range(numCol):
                if 5 <= board[i][j] <= 7:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
