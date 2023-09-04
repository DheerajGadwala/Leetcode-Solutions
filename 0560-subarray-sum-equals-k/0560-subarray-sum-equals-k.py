class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = [0]
        for i in nums:
            pref.append(pref[-1] + i)
        mp = dict()
        ans = 0
        for i in range(len(pref)):
            q = pref[i] - k
            ans += mp.get(q, 0)
            mp[pref[i]] = mp.get(pref[i], 0) + 1
        return ans