class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ar: int) -> int:
        n = len(rocks)
        rs = [(capacity[i], rocks[i]) for i in range(n)]
        rs.sort(key = lambda x: x[0] - x[1])
        cnt = 0
        i = 0
        while i < n and ar - (rs[i][0] - rs[i][1]) >= 0:
            ar -= (rs[i][0] - rs[i][1])
            i += 1
        return i
            