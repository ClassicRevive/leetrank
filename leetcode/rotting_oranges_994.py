# this is my own raw solution, which is accepted but slower than others. Still need to study editorial

# optimisation: Use tuples
# alternative: Instead of 2 queues approach, use a singel queue and a sentinel to separate between the levels
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS with 2 queues. Each time we empty a queue, we finish a wave.
        from collections import deque
        nrows = len(grid)
        ncols = len(grid[0])
        visited = [[False]*ncols for i in range(nrows)]

        curr_level = deque()
        next_level = deque()
        n_oranges = 0
        n_rotten = 0
        mins = 0

        # get position of rotten oranges
        # also count the number of oranges
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] > 0:
                    n_oranges += 1

                if grid[row][col] == 2:
                    next_level.append([row, col])
                    visited[row][col] = True
                    n_rotten += 1
        
        def is_valid(node):
            row = node[0]
            col = node[1]
            
            return 0 <= row < nrows and 0 <= col < ncols and grid[row][col] == 1

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.pop()
                for off in dirs:
                    new_node = list(node)
                    new_node[0] += off[0]
                    new_node[1] += off[1]
                    new_r = new_node[0]
                    new_c = new_node[1]

                    # found a new orange
                    if is_valid(new_node) and not visited[new_r][new_c]:
                        next_level.append(new_node)
                        visited[new_r][new_c] = True  # mark as visited upon detection
                        n_rotten += 1

            if next_level:  # if there are more oranges to rot, then increase waves by 1
                mins += 1
        
        # after oranges rotting in waves, check if n_rotten == n_oranges
        print(n_rotten)
        print(n_oranges)
        if n_rotten == n_oranges:
            return mins
        else:
            return -1
        