class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            sm = nums[i] + nums[j]
            if sm == target:
                return [i+1, j+1]
            elif sm < target:
                i += 1
            else:
                j -= 1
        return None