class Solution:
    def canMeasureWater(self, j1: int, j2: int, tar: int) -> bool:
        q = [(0, 0)]
        visited = {(0, 0), }
        while len(q) != 0:
            a, b = q.pop()
            if a == tar or b == tar or a + b == tar:
                return True
            k = (j1, b)
            if k not in visited:
                q.append(k)
                visited.add(k)
            k = (a, j2)
            if k not in visited:
                q.append(k)
                visited.add(k)
            k = (0, b)
            if k not in visited:
                q.append(k)
                visited.add(k)
            k = (a, 0)
            if k not in visited:
                q.append(k)
                visited.add(k)
            k = (min(a+b, j1), a + b - min(a+b, j1))
            if k not in visited:
                q.append(k)
                if q[-1][0] == tar or q[-1][1] == tar or sum(q[-1]) == tar:
                    return True
                visited.add(k)
            k = (a + b - min(a+b, j2) , min(a+b, j2))
            if k not in visited:
                q.append(k)
                if q[-1][0] == tar or q[-1][1] == tar or sum(q[-1]) == tar:
                    return True
                visited.add(k)
        return False