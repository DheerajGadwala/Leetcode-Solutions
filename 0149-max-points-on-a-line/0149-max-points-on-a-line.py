class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        n = len(points)
        lines = dict()
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                m = math.inf if x2 == x1 else (y2 - y1) / (x2 - x1)
                c = y1 - m * x1
                lines[(m, x1 if x1 == x2 else c)] = 0

        for x, y in points:
            for m, c in lines:
                if m == math.inf:
                    lines[(m, c)] += 1 if x == c else 0
                elif abs(y - (m * x + c)) < 10**-6:
                    lines[(m, c)] += 1
        mx = 0
        for line in lines:
            mx = max(mx, lines[line])
        return mx
                
        