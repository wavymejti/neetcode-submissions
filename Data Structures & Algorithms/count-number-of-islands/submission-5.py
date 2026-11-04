class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1],[0,-1]]
        numIsland = 0
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
                
            grid[r][c] = '0'
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row,col)
                    numIsland += 1
        return numIsland