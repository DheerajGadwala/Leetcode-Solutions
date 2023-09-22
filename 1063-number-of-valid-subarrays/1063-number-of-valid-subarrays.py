class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        s = []
        for i in range(len(nums)):
            while len(s) > 0 and nums[i] < nums[s[-1]]:
                ans += i - s.pop()
            s.append(i)
        while len(s)>0:
            ans += len(nums) - s.pop()
        return ans