class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def cnt(t):
            ret = 0
            i = 0
            while i < n - 1:
                v = nums[i+1]-nums[i]
                if v <= t:
                    ret += 1
                    i += 2
                else:
                    i += 1
            return ret
        
        l, h = 0, 10**9
        ret = h
        while l <= h:
            m = (l+h) // 2
            c = cnt(m)
            if c < p:
                l = m + 1
            elif c >= p:
                ret = m
                h = m - 1
        
        return ret