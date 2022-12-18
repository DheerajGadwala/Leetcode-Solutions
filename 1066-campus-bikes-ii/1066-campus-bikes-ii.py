class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        
        @cache
        def res(i = 0, state = 0):
            if i == n:
                return 0
            else:
                u, v = workers[i]
                s = 1
                ret = math.inf
                for j in range(m):
                    if state & s == 0:
                        x, y = bikes[j]
                        ret = min(ret, abs(x-u) + abs(y-v) + res(i+1, state | s))
                    s <<= 1
                return ret
                
        
        return res()
        