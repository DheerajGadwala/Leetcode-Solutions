class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = []
        for i in range(1, n):
            climb = heights[i] - heights[i-1]
            if climb <= 0:
                continue
            elif bricks >= climb:
                bricks -= climb
                heappush(q, -climb)
            elif ladders > 0:
                if len(q) > 0 and climb < -q[0]:
                    bricks += -heappop(q) - climb
                    heappush(q, -climb)
                ladders -= 1
            else:
                return i - 1
        return n - 1