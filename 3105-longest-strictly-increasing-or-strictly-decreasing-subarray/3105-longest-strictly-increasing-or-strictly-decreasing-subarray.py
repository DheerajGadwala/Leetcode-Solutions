class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx, currInc, currDec = 1, 1, 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currInc += 1
                currDec = 1
            elif nums[i] < nums[i-1]:
                currDec += 1
                currInc = 1
            else:
                currInc = 1
                currDec = 1
            mx = max(mx, currInc, currDec)
        return mx
        