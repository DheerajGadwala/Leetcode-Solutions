class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, h = 0, n-1
        lb, rb = -1, -1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                rb = m
                l = m + 1
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        l, h = 0, n-1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                lb = m
                h = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        return [lb, rb]