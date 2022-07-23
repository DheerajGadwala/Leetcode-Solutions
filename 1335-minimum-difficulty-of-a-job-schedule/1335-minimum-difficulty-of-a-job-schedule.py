class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        
        @cache
        def res(pos = 0, d = d, mx = 0):
            if d == 0 and pos != len(jd):
                return math.inf
            elif d == 0 and pos == len(jd):
                return 0
            elif d == 0 or pos == len(jd):
                return math.inf
            else:
                return min(res(pos+1, d, max(mx, jd[pos])), max(mx, jd[pos]) + res(pos+1, d-1, 0))
        
        ret = res()
        ret = -1 if ret == math.inf else ret
        
        return ret
