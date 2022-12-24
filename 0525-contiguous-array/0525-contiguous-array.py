class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = dict()
        n = len(nums)
        ones = 0
        zeroes = 0
        ans = 0
        mp[0] = -1
        for i in range(n):
            if nums[i] == 1:
                ones += 1
            else:
                zeroes += 1
            diff = ones - zeroes
            if diff not in mp:
                mp[diff] = i
            else:
                ans = max(ans, i - mp[diff])
        
        return ans