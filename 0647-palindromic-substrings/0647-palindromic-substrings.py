class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = 1
            ans += dp[i][i]
        
        for j in range(1, n):
            for i in range(n):
                if i + j < n:
                    dp[i][i + j] = 1 if s[i] == s[i + j] and (j ==1 or dp[i + 1][i + j - 1] != 0) else 0
                    ans += dp[i][i + j]
                else:
                    break
                    
        return ans
        