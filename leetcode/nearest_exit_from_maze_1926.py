# shortest path to exit in grid BFS algorithm. Note the is_valid and usage of queue.
# my own solution, fast enough, but can be improved. Fun problem

# optimisation: instead of backtracking, just record the current distance and update as we go
# optimisation: use tuple for dirs instead of list

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs algorithm by coordinates
        nrows = len(maze)
        ncols = len(maze[0])

        queue = deque()
        visited = [[False]*ncols for i in range(nrows)]
        visited[entrance[0]][entrance[1]] = True
        queue.append(entrance)
        backtrack = {}

        def is_valid(coord):
            # check if current coordinate is valid
            row = coord[0]
            col = coord[1]
            return 0 <= row < nrows and 0 <= col < ncols and maze[row][col] == '.'
        
        def is_exit(coord):
            # check if current coordinate is an exit
            row = coord[0]
            col = coord[1]
            return (row in [0, nrows-1] or col in [0, ncols-1]) and coord != entrance

        # legal directions
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            curr = queue.popleft()
            
            # once we find the exit, backtrack right away
            if is_exit(curr):
                steps = 0
                while curr != entrance:
                    curr = backtrack[str(curr)]
                    steps += 1
                
                return steps

            for offset in dirs:
                new_curr = list(curr)
                for i in range(len(curr)):  # building new prospective coordinate
                    new_curr[i] += offset[i]
                new_r = new_curr[0]
                new_c = new_curr[1]

                # adding new coordinates to search
                if is_valid(new_curr) and not visited[new_r][new_c]:
                    queue.append(new_curr)
                    visited[new_curr[0]][new_curr[1]] = True
                    backtrack[str(new_curr)] = curr

        return -1
                