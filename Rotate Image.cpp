class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // for (int i = 0; i < n/2; i++)
        //     for (int j = 0 ; j < n - 1 -  2 * i; j++)
        //     {
        //         swap(matrix[i][i+j], matrix[i+j][n-1-i]);
        //         swap(matrix[i][i+j], matrix[n-1-i][n-1-i-j]);
        //         swap(matrix[i][i+j], matrix[n-1-i-j][i]);
        //     }
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++)
                swap(matrix[i][j], matrix[j][i]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n/2; j++)
                swap(matrix[i][j], matrix[i][n-1-j]);
    }
};
