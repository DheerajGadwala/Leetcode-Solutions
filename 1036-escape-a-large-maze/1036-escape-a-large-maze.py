import heapq
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        def bfs(s, t, blocked):
            q = [s]
            blocked.add(tuple(s))
            while len(q) != 0:
                x, y = q.pop()
                if (abs(s[0]-x) + abs(s[1]-y) >= 200) or ([x, y] == t):
                    return True
                neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for n in neighbours:
                    if n[0] > -1 and n[0] < 1000000 and n[1] > -1 and n[1] < 1000000 and n not in blocked:
                        q.append(n)
                        blocked.add(n)
            return False
        
        blocked = {(a[0], a[1]) for a in blocked}
        return bfs(source, target, set(blocked)) and bfs(target, source, set(blocked))
                