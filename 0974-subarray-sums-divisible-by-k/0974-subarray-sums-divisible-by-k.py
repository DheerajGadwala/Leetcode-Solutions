class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums[0] %= k
        for i in range(1, n):
            nums[i] += nums[i-1]
            nums[i] %= k
        mem = defaultdict(int)
        mem[0] = 1
        ans = 0
        for i in nums:
            ans += mem[i]
            mem[i] += 1
        return ans