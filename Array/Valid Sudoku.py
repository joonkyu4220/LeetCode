class Solution(object):
    
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row_dic = {i:[] for i in range(9)}
        col_dic = {i:[] for i in range(9)}
        cel_dic = {i:[] for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_dic[i] \
                       or board[i][j] in col_dic[j] \
                       or board[i][j] in cel_dic[i//3 * 3 + j//3]:
                        return False
                    else:
                        row_dic[i].append(board[i][j])
                        col_dic[j].append(board[i][j])
                        cel_dic[i//3 * 3 + j//3].append(board[i][j])
                        
        return True
                        
        
