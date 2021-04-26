class Solution(object):
    
    def __init__(self):
        self.found = False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def helper(board, check, word, numRow, numCol, startR, startC):
            if len(word) == 0:
                self.found = True
                return
            if startR < 0 or startR >= numRow or startC < 0 or startC >= numCol:
                return
            if board[startR][startC] == word[0] and check[startR][startC]:
                check[startR][startC] = 0
                helper(board, check, word[1:], numRow, numCol, startR-1, startC)
                helper(board, check, word[1:], numRow, numCol, startR+1, startC)
                helper(board, check, word[1:], numRow, numCol, startR, startC-1)
                helper(board, check, word[1:], numRow, numCol, startR, startC+1)
        
        numRow = len(board)
        numCol = len(board[0])
        
        for r in range(numRow):
            for c in range(numCol):
                check = [[1 for _ in range(numCol)] for _ in range(numRow)]
                helper(board, check, word, numRow, numCol, r, c)
                if self.found:
                    return self.found
        
        return False
                
                
        
        
