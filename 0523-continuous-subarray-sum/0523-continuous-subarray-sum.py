class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in mp:
                mp[s%k] = i + 1
            elif mp[s%k] < i:
                return True
        return False
        