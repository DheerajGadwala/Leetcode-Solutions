class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        currMx = nums[0]
        currMn = nums[0]
        sm = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] + currMx <= nums[i]:
                currMx = nums[i]
            else:
                currMx += nums[i]
            mx = max(mx, currMx)
            if nums[i] + currMn >= nums[i]:
                currMn = nums[i]
            else:
                currMn += nums[i]
            mn = min(mn, currMn)
            sm += nums[i]
        return mx if sm == mn else max(mx, sm - mn)