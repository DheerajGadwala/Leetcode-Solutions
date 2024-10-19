class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * (n+1)
        i, j = 0, 1
        while j < n:
            if s[i] == s[j]:
                i+=1
                j+=1
                lps[j]=i
            elif i == 0:
                j+=1
            else:
                i=lps[i]
        return s[:lps[-1]]