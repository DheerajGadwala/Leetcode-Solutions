class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def res(pos = 0, bought = False):
            nonlocal n
            if pos >= n:
                return 0
            elif bought:
                return max(nums[pos] + res(pos + 2, False), res(pos + 1, True))
            else:
                return max(-nums[pos] + res(pos + 1, True), res(pos + 1, False))
        return res()
