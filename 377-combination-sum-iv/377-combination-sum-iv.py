class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def res(pos = 0, sm = target):
            if pos == len(nums) or sm < 0:
                return 0
            elif sm == 0:
                return 1
            else:
                return res(0, sm-nums[pos]) + res(pos+1, sm)
        
        return res()
            