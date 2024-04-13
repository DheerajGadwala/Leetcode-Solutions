class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = n // 2
        ans = 0
        while i > -1:
            if nums[i] > k:
                ans += nums[i] - k
            else:
                break
            i -= 1
        i = n // 2
        while i < n:
            if nums[i] < k:
                ans += k - nums[i]
            else:
                break
            i += 1
        return ans