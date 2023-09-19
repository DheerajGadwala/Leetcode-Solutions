class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = None
        for i in nums:
            x = abs(i)
            if nums[x-1] < 0:
                return x
            else:
                nums[x-1] *= -1