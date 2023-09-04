class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        rs = 0
        ans = -math.inf
        for i in nums:
            rs += i
            ans = max(ans, rs, total - rs + i)
        return ans