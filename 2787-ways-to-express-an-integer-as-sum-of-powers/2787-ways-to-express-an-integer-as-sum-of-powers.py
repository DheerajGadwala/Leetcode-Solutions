class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        nums = []
        i = 1
        while i**x <= n:
            nums.insert(0, i**x)
            i += 1
        
        mod = 10**9+7
        
        @cache
        def res(i = n, j = 0):
            if i == 0:
                return 1
            elif j == len(nums):
                return 0
            elif i >= nums[j] > 0:
                return (res(i - nums[j], j + 1) + res(i, j + 1)) % mod
            else:
                return res(i, j + 1)
        
        return res()
            