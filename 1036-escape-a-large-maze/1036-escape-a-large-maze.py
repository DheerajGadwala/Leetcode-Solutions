import heapq
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        escapeDist = len(blocked)
        
        def dfs(s, t, blocked):
            nonlocal escapeDist
            stk = [s]
            blocked.add(tuple(s))
            while len(stk) != 0:
                x, y = stk.pop()
                if (abs(s[0]-x) + abs(s[1]-y) >= escapeDist):
                    return True
                neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for n in neighbours:
                    if n[0] > -1 and n[0] < 1000000 and n[1] > -1 and n[1] < 1000000 and n not in blocked:
                        stk.append(n)
                        blocked.add(n)
            return (t[0], t[1]) in blocked
        
        blocked = {(a[0], a[1]) for a in blocked}
        return dfs(source, target, set(blocked)) and dfs(target, source, set(blocked))