class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        lps = [0] * n
        i, j = 1, 0
        while i < n:
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j-1]
            else:
                i += 1
        i, j = 0, 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
        return -1 if j != n else i - j