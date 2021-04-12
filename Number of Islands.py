class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numRow = len(grid)
        numCol = len(grid[0])
        
        def eraser(grid, i, j):
            if i < 0 or j < 0 or i >= numRow or j >= numCol or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            
            eraser(grid, i-1, j)
            eraser(grid, i+1, j)
            eraser(grid, i, j+1)
            eraser(grid, i, j-1)
        
        ans = 0
        
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == '1':
                    ans += 1
                    eraser(grid, i, j)
        
        return ans
