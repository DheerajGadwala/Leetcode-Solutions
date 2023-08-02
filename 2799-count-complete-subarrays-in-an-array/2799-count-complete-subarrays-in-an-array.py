class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        x = len(set(nums))
        mp = dict()
        i, j = 0, 0
        ans = 0
        while j < n:
            if len(mp) < x:
                mp[nums[j]] = mp.get(nums[j], 0) + 1
                j+=1
                if len(mp) == x:
                    ans+=n-j+1
            elif mp[nums[i]] > 1:
                mp[nums[i]] -= 1
                i+=1
                ans+=n-j+1
            else:
                mp[nums[j]] += 1
                j += 1
        while i < n:
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0:
                break
            else:
                ans+=1
                i+=1
        return ans
        