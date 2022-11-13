class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        intervals = []
        n = len(s)
        for i in range(n):
            j = 0
            while i - j > -1 and i + j < n and s[i - j] == s[i + j]:
                st, e = i - j, i + j
                if e - st + 1 >= k:
                    intervals.append([st, e])
                j += 1
        for i in range(n - 1):
            j = 0
            while i - j > -1 and i + 1 + j < n and s[i - j] == s[i + 1 + j]:
                st, e = i - j, i + 1 + j
                if e - st + 1 >= k:
                    intervals.append([st, e])
                    break
                j += 1
        intervals.sort(key = lambda x: x[1])
        t = -1
        ans = 0
        for s, e in intervals:
            if s > t:
                t = e
                ans += 1
        return ans
            