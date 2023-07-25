class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[-1]
        for i in range(n-1, 0, -1):
            if nums[i] >= nums[i - 1]:
                nums[i - 1] += nums[i]
                ans = max(ans, nums[i-1])
            else:
                ans = max(ans, nums[i-1])
        return ans