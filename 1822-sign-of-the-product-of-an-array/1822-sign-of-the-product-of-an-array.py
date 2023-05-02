class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if n == 0:
                ans = 0
            else:
                ans *= n // abs(n)
        return ans