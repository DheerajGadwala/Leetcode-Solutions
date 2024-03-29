class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in mp:
                mp[s%k] = i
            elif i - mp[s%k] > 1:
                return True
        return False
        