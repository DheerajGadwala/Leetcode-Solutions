class Solution:
    def putMarbles(self, nums: List[int], k: int) -> int:
        n = len(nums)
        x = []
        for i in range(n - 1):
            x.append(nums[i] + nums[i + 1])
        x.sort()
        mx, mn = 0, 0
        for i in range(k - 1):
            mx += x[len(x) - i - 1]
            mn += x[i]
        return mx - mn
        
    """
        @cache
        def mn(pos = 0, k = k - 1):
            if k == 0:
                return 0
            elif pos == n - 1:
                return math.inf
            else:
                return min(nums[pos] + nums[pos+1] + mn(pos + 1, k - 1), mn(pos + 1, k))
        
        @cache
        def mx(pos = 0, k = k - 1):
            if k == 0:
                return 0
            elif pos == n - 1:
                return -math.inf
            else:
                return max(nums[pos] + nums[pos + 1] + mx(pos + 1, k - 1), mx(pos + 1, k))
        
        return mx() - mn()
    """
            