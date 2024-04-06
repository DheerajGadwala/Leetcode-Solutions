class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        
        xpy = [math.inf, -math.inf]
        xmy = [math.inf, -math.inf]
        xpy_val = [None, None]
        xmy_val = [None, None]
        for i in range(len(points)):
            x, y = points[i]
            if x+y < xpy[0]:
                xpy[0] = x+y
                xpy_val[0] = i
            if x+y > xpy[1]:
                xpy[1] = x+y
                xpy_val[1] = i
            if x-y < xmy[0]:
                xmy[0] = x-y
                xmy_val[0] = i
            if x-y > xmy[1]:
                xmy[1] = x-y
                xmy_val[1] = i

        l = xpy_val + xmy_val
        ans = math.inf
        for j in l:
            xpy = [math.inf, -math.inf]
            xmy = [math.inf, -math.inf]
            for i in range(len(points)):
                if j == i:
                    continue
                x, y = points[i]
                xpy = [min(xpy[0], x+y), max(xpy[1], x+y)]
                xmy = [min(xmy[0], x-y), max(xmy[1], x-y)]
            ans = min(ans, max(xpy[1]-xpy[0], xmy[1]-xmy[0]))

        return ans
        