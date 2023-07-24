class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        
        n = len(nums)
        
        @cache
        def res(pos = 1, par = nums[0] % 2):
            if pos == n:
                return 0
            elif par == nums[pos] % 2:
                return max(nums[pos] + res(pos + 1, par), res(pos+1, par))
            else:
                return max(nums[pos] - x + res(pos + 1, nums[pos] % 2), res(pos + 1, par))
        
        return nums[0] + res()