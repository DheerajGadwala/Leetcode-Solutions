class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        
        m = len(mat)
        n = len(mat[0])
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + mat[i][j]
        
        ans = 0
        
        for i in range(m + 1):
            for j in range(i + 1, m + 1):
                h = dict()
                for k in range(n + 1):
                    val = dp[j][k] - dp[i][k]
                    ans += 0 if val - target not in h else h[val - target]
                    if val in h:
                        h[val] += 1
                    else:
                        h[val] = 1
        return ans