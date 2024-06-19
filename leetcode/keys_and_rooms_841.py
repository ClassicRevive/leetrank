class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # run dfs from root and check if whole graph traversed.
        n_rooms = len(rooms)
        visited = [False]*n_rooms

        def dfs(curr):
            if not visited[curr]:
                visited[curr] = True

                for next_room in rooms[curr]:
                    dfs(next_room)

        dfs(0)
        return sum(visited) == n_rooms
