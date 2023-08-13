class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @cache
        def res(pos = 0):
            if pos == n:
                return True
            ret = False
            if pos + 1 < n:
                ret |= nums[pos] == nums[pos + 1] and res(pos + 2)
            if pos + 2 < n:
                ret |= nums[pos] == nums[pos + 1] and nums[pos + 1] == nums[pos + 2] and res(pos + 3)
                ret |= nums[pos] + 1 == nums[pos + 1] and nums[pos + 1] + 1 == nums[pos + 2] and res(pos + 3)
            return ret
        
        return res()