class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def res(pos = 0):
            if pos == len(nums):
                return 0
            ret = 0
            for j in range(pos + 1, len(nums)):
                if nums[j] > nums[pos]:
                    ret = max(ret, 1 + res(j))
            return ret
        
        ret = 0
        for i in range(len(nums) - 1, -1, -1):
            ret = max(ret, res(i))
        
        return ret + 1