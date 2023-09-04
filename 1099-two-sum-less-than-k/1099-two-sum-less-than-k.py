class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ret = -1
        while i < j:
            if nums[i] + nums[j] < k:
                ret = max(nums[i] + nums[j], ret)
                i += 1
            else:
                j -= 1
        return ret