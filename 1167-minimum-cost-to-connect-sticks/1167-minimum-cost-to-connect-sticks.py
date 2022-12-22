class Solution:
    def connectSticks(self, q: List[int]) -> int:
        heapify(q)
        ret = 0
        while len(q) != 1:
            a, b = heappop(q), heappop(q)
            ret += a + b
            heappush(q, a + b)
        return ret