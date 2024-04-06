class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1
        ans = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                curr = 1
            else:
                curr += 1
            ans += curr
        return ans
        