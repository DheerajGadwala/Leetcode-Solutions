class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = dict()
        for t in tasks:
            if t not in d:
                d[t] = 0
            d[t] += 1
        ans = 0
        for t in d:
            if d[t] == 1:
                return -1
            elif d[t] % 3 == 0:
                ans += d[t] // 3
            elif d[t] % 3 == 1:
                ans += (d[t] - 4) // 3 + 2
            elif d[t] % 3 == 2:
                ans += d[t] // 3 + 1
        return ans