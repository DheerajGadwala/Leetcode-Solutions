class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def res(l, r):
            if l > r:
                return 0
            left = 1 if l - 1 == -1 else nums[l - 1]
            right = 1 if r + 1 == n else nums[r + 1]
            ret = nums[l] * left * right
            for i in range(l, r+1):
                ret = max(ret, res(l, i-1) + res(i+1, r) + nums[i] * left * right)
            return ret
        return res(0, n-1)