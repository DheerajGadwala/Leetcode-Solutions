class Solution:
    def maxPerformance(self, n: int, s: List[int], e: List[int], k: int) -> int:
        se = [(-e[i], s[i]) for i in range(n)]
        h = []
        heapify(se)
        MOD = 10**9+7
        curr, ans = 0, 0
        for i in range(n):
            eff, spd = heappop(se)
            if len(h) < k:
                curr += spd
                heappush(h, spd)
                ans = max(ans, -eff*curr)
            else:
                popped = heappop(h)
                curr -= popped
                curr += spd
                ans = max(ans, -eff*curr)
                curr -= spd
                curr += max(spd, popped)
                heappush(h, max(spd, popped))
            
        return ans % MOD