class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9+7
        n = len(s)
        for i in range(n):
            nums[i] += d if s[i] == 'R' else -d
        nums.sort()
        i = n
        j = 1
        ans = 0
        for k in nums:
            ans += (j - i) * k
            ans %= mod
            i -= 1
            j += 1
        return ans
        
                
                
            