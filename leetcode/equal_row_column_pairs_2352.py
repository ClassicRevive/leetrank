class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
            Store the row variations in a hashmap and column variations in a separate hashamap.
            Then loop through rows and count matches with columns (O(n^2))
        '''
        from collections import defaultdict
        n = len(grid)
        
        # store row and column occurences in hashmaps
        rows = defaultdict(int)
        cols = defaultdict(int)
        for r in range(n):  # store row as a string since lists aren't valid keys
            rows[str(grid[r])] += 1

        for c in range(n):
            # build column
            col = []
            for r in range(n):
                col.append(grid[r][c])
            cols[str(col)] += 1
        
        pairs = 0
        for row, count in rows.items():
            pairs += (count * cols[row])
        
        return pairs

            