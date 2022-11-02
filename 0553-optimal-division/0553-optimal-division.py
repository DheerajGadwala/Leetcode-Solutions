class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        @cache
        def res(l = 0, h = len(nums) - 1):
            if l == h:
                return [nums[l], nums[l], str(nums[l]), str(nums[l])]
            mx, mn = -math.inf, math.inf
            mxDiv, mnDiv = [], []
            for i in range(l, h):
                lmx, lmn, lmxDiv, lmnDiv = res(l, i)
                rmx, rmn, rmxDiv, rmnDiv = res(i + 1, h)
                if lmx / rmn > mx:
                    mx = lmx / rmn
                    if i + 1 != h:
                        mxDiv = lmxDiv + '/(' + rmnDiv + ')' 
                    else:
                        mxDiv = lmxDiv + '/' + rmnDiv 
                if lmn / rmx < mn:
                    mn = lmn / rmx
                    if i + 1 != h:
                        mnDiv = lmnDiv + '/(' + rmxDiv + ')'
                    else:
                        mnDiv = lmnDiv + '/' + rmxDiv
            return mx, mn, mxDiv, mnDiv

        return res()[2]
                
            
                