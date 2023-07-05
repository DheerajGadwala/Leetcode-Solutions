class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = -1
        curr = 0
        ans = 0
        for i in nums:
            if i != 0:
                curr += i
            else:
                ans = max(ans, prev+curr)
                prev = curr
                curr = 0
        return max(ans, prev + curr)
                