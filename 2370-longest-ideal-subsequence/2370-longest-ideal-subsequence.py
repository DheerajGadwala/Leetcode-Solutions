class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        nums = [ord(i) - ord('a') for i in s]
        n = len(nums)
        dp = [0] * 26
        for i in range(n):
            c = nums[i]
            best = 0
            for j in range(max(0, c - k), min(c + k + 1, 26)):
                best = max(best, dp[j])
            dp[c] = best + 1
        return max(dp)
                