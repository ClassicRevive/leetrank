class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(grid, r, c):
            nr = len(grid)
            nc = len(grid[0])

            grid[r][c] ='0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                dfs(grid, r-1, c)
            if r+1 < nr and grid[r+1][c] == '1':
                dfs(grid, r+1, c)
            if c-1 >= 0 and grid[r][c-1] == '1':
                dfs(grid, r, c-1)
            if c+1 < nc and grid[r][c+1] == '1':
                dfs(grid, r, c+1)
            
            return grid

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    print(grid)
                    grid = dfs(grid, r, c)
        
        return islands

if __name__ == '__main__':
    print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))