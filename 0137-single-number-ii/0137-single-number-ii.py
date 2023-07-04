class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cnt = dict()
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
        for n in cnt:
            if cnt[n] == 1:
                return n
                