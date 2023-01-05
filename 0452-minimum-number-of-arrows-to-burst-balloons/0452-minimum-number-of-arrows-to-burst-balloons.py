class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        ans = 0
        p = -math.inf
        for s, e in points:
            if s > p:
                ans += 1
                p = e
        return ans