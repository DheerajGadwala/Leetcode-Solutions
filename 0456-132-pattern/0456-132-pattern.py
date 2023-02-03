class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        for i in nums:
            mn = i
            while len(s) != 0 and s[-1][0] <= i:
                mn = min(mn, s.pop()[1])
            if len(s) > 0 and s[-1][1] < i and i < s[-1][0]:
                return True
            s.append((i, mn))
        return False