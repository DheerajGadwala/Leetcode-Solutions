class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            if i == 0:
                curr += 1
            else:
                curr = 0
            ans += curr
        return ans