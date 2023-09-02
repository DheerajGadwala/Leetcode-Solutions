class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        lps = [0] * n
        i, j = 1, 0
        while i < n:
            if b[i] == b[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
        prev, j = -1, 0
        cnt = 1
        print(lps)
        while prev != j:
            prev = j
            i = 0
            while i < m and j < n:
                if a[i] == b[j]:
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == n:
                return cnt
            cnt += 1
        return -1