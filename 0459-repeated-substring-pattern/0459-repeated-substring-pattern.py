class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i, j = 1, 0
        lps = [0] * n
        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i+= 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
        t = s + s
        m = 2 * n
        i, j = 1, 0
        print(t, s)
        while i < m - 1 and j < n:
                if t[i] == s[j]:
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        return j == n
        