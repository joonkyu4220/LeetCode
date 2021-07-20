class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rowMap (9, vector<int>(9, 0));
        vector<vector<int>> colMap (9, vector<int>(9, 0));
        vector<vector<vector<int>>> cellMap(3, vector<vector<int>>(3, vector<int>(9, 0)));
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                if (board[i][j] != '.')
                {
                    int cur = board[i][j] - '1';
                    if (rowMap[i][cur] || colMap[j][cur] || cellMap[i/3][j/3][cur]) return false;
                    rowMap[i][cur] = 1;
                    colMap[j][cur] = 1;
                    cellMap[i/3][j/3][cur] = 1;
                }
        return true;
    }
};
