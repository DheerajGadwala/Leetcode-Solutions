class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        i, j = (0, len(nums) - 1)
        while i < j:
            n = nums[i] + nums[j]
            if n >= k:
                j -= 1
            else:
                ans = max(ans, n)
                i += 1
        return ans