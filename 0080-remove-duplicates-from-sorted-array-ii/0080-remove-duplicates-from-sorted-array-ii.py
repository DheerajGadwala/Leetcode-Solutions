class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        p1, p2 = None, None
        while j < n:
            if p1 == p2 and nums[j] == p2:
                j += 1
            else:
                p1 = p2
                p2 = nums[j]
                nums[i] = nums[j]
                i += 1
                j += 1
        return i