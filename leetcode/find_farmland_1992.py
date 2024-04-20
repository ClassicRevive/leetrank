class Solution:
    '''
        This question is very good practice at applying DFS or BFS algorithm.
        We need to record coordinates already visited, and need to record the top left and bottom
        # right of the current island (connected component)
    '''
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        global maxrow
        global maxcol
        
        def in_farm(r, c, nr, nc):
            return 0 <= r < nr and 0 <= c < nc

        def dfs(land, r, c, visited):
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            global maxrow
            global maxcol
            nr = len(land)
            nc = len(land[0])
            
            # update maxrow and maxcol of current farmland
            visited[r][c] = 1
            maxrow = max(r, maxrow)
            maxcol = max(c, maxcol)

            for dir in dirs:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if in_farm(new_r, new_c, nr, nc) and not visited[new_r][new_c] and land[new_r][new_c] == 1:
                    dfs(land, new_r, new_c, visited)
        
        
        farmlands = []
        curr = []
        nr = len(land)
        nc = len(land[0])
        visited = [[0]*nc for i in range(nr)] # build visited matrix to store if a cell was visited

        for r in range(len(land)):
            for c in range(len(land[0])):
                maxrow = maxcol = 0
                if land[r][c] == 1 and not visited[r][c]:
                    curr.extend([r, c])  # top left
                    dfs(land, r, c, visited)
                    curr.extend([maxrow, maxcol])  # bottom right
                    farmlands.append(curr)
                    
                    curr = []
        return farmlands


print(Solution().findFarmland(land=[[1,1],[1,1]]))

            


        