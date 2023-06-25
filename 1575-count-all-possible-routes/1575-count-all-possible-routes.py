class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9+7
        @cache
        def res(u = start, f = fuel):
            if f < 0:
                return 0
            ret = 1 if u == finish else 0
            for i in range(n):
                if i != u:
                    ret += res(i, f - abs(locations[i] - locations[u]))
                    ret %= mod
            return ret
        return res()