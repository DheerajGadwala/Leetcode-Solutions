import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        q = []
        for i in cnt:
            heappush(q, [-cnt[i], i])
        ans = 0
        while len(q) != 0:
            removed = []
            for i in range(n+1):
                if len(q) != 0:
                    r = heappop(q)
                    r[0] += 1
                    if r[0] != 0:
                        removed.append(r)
                ans += 1
                if len(removed) == 0 and len(q) == 0:
                    break
            for r in removed:
                heapq.heappush(q, [r[0], r[1]])
        return ans
        
        