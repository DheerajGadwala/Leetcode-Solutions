class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def res(pos = 0, steal = True):
            if pos == len(nums):
                return 0
            elif steal:
                return max(nums[pos] + res(pos+1, False), res(pos+1, True))
            else:
                return res(pos+1, True)
        
        return res()
                
            