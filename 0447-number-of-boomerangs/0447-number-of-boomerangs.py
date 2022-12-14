class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            x, y = points[i]
            mp = dict()
            for a, b in points:
                dist = ((a - x) ** 2 + (b - y) ** 2) ** 0.5
                if dist not in mp:
                    mp[dist] = 0
                mp[dist] += 1
            for d in mp:
                x = mp[d]
                ans += x * (x-1)
        
        return ans