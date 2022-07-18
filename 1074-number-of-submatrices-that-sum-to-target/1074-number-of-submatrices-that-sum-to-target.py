class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        
        # O(n^3) => Similar to count of subarrays whose sum equals target
        
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

# first attempt: O(n^4) solution
    
# class Solution:
#     def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        
#         m = len(mat)
#         n = len(mat[0])
        
#         dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
#         for i in range(m):
#             for j in range(n):
#                 dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + mat[i][j]
        
#         ans = 0
        
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 for k in range(i):
#                     for l in range(j):
#                         if dp[i][j] - dp[k][j] - dp[i][l] + dp[k][l] == target:
#                             ans += 1
        
#         return ans