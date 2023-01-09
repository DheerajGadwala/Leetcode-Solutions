class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        mp = dict()
        future = [None] * n
        for i in range(n - 1, -1, -1):
            if rains[i] not in mp:
                future[i] = math.inf
            else:
                future[i] = mp[rains[i]]
            mp[rains[i]] = i
        ans = []
        full = []
        full_set = set()
        for i in range(n):
            if rains[i] > 0 and rains[i] not in full_set:
                heappush(full, (future[i], rains[i]))
                full_set.add(rains[i])
                ans.append(-1)
            elif rains[i] > 0:
                return []
            elif len(full) > 0:
                f, r = heappop(full)
                full_set.remove(r)
                ans.append(r)
            else:
                # any number can be appended here
                ans.append(1)
        return ans