class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        srev = s[::-1]
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(len(s)):
                dp[i+1][j+1] = max(dp[i][j] + (1 if s[i] == srev[j] else 0), dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]