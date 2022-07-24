class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        
        srev = s[::-1]
        
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i+1][j], dp[i][j+1])
                if s[i] == srev[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], 1 + dp[i][j])
        
        return len(s) - dp[-1][-1]