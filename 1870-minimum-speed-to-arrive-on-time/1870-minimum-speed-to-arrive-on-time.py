class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 > hour:
            return -1
        
        n = len(dist)
        
        def time(speed):
            t = 0
            for i in range(n - 1):
                t += dist[i] / speed
                t = math.ceil(t)
            t += dist[-1]/speed
            return t
        
        l, h = 1, 10**9
        ans = -1
        while l <= h:
            m = (l + h) // 2
            t = time(m)
            if t > hour:
                l = m + 1
            else:
                ans = m
                h = m - 1
        return ans