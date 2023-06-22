class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        total = 2**n - 1
        mod = 10**9+7
        @lru_cache(None)
        def res(i, mask):
            if mask == total:
                return 1
            k = 1
            ret = 0
            for j in nums:
                if mask & k == 0 and (i % j == 0 or j % i == 0):
                    ret += res(j, mask | k)
                    ret %= mod
                k <<= 1
            return ret
        j = 1
        ans = 0
        for i in nums:
            ans += res(i, j)
            ans %= mod
            j <<= 1
        return ans