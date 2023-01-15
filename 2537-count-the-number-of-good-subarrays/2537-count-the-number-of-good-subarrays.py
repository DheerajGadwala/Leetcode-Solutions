class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        cnt = defaultdict(int)
        i, j = 0, 0
        n = len(nums)
        
        curr = 0
        ans = 0
        
        while j < n or curr >= k:
            if curr < k:
                ans += i
                x = nums[j]
                curr -= (cnt[x] * (cnt[x] - 1)) // 2
                cnt[x] = cnt.get(x, 0) + 1
                curr += (cnt[x] * (cnt[x] - 1)) // 2
                j += 1
            else:
                x = nums[i]
                curr -= (cnt[x] * (cnt[x] - 1)) // 2
                cnt[x] -= 1
                curr += (cnt[x] * (cnt[x] - 1)) // 2
                i += 1

        return ans + i