class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in range(1, n - 1):
            if i in d and d[i] == 1 and i != n - 1:
                continue
            else:
                return False
        return n - 1 in d and d[n - 1] == 2
            