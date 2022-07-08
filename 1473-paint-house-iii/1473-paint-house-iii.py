class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        
        @cache
        def res(pos = 0, prev = -1, splits = 0):
            if splits > target:
                return math.inf
            elif pos == len(houses) and splits == target:
                return 0
            elif pos == len(houses):
                return math.inf
            elif houses[pos] != 0 and prev == houses[pos]:
                return res(pos + 1, houses[pos], splits)
            elif houses[pos] != 0 and prev != houses[pos]:
                return res(pos + 1, houses[pos], splits+1)
            else:
                ret = math.inf
                for i in range(1, n+1):
                    if prev == i:
                        ret = min(ret, cost[pos][i-1] + res(pos+1, prev, splits))
                    else:
                        ret = min(ret, cost[pos][i-1] + res(pos+1, i, splits+1))
                return ret
        
        ans = res()
        
        return -1 if ans == math.inf else ans