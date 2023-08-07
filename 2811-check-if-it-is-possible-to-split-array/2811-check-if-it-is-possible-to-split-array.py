class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        
        @cache
        def checkSum(l, r):
            sm = 0
            for i in range(l, r+1):
                sm += nums[i]
            return sm >= m
        
        @cache
        def res(l = 0, r = len(nums) - 1):
            if l == r:
                return True
            else:
                ret = False
                for i in range(l, r):
                    if (checkSum(l, i) or l == i) and (checkSum(i+1, r) or i+1 == r):
                        ret |= (res(l, i) and res(i+1, r))
                return ret
        
        return res()