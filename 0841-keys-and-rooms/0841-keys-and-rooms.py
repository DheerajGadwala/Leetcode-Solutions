class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        q = [0]
        while len(q) != 0:
            u = q.pop(0)
            for v in rooms[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        allVisited = True
        for i in visited:
            allVisited &= i
        return allVisited