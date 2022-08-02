import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for i in matrix:
            for j in i:
                if len(h) == k and -h[0] > j:
                    heapq.heappop(h)
                    heapq.heappush(h, -j)
                elif len(h) < k:
                    heapq.heappush(h, -j)
        return -h[0]