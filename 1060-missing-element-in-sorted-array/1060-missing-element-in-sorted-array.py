class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(1, len(nums)):
            c += nums[i] - nums[i-1] - 1
            if c >= k:
                return nums[i] - c + k - 1
        return nums[-1] - c + k
        