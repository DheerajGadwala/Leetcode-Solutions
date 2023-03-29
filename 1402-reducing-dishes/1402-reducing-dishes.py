class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ret = 0
        cur = 0
        satisfaction.sort()
        while len(satisfaction) != 0 and satisfaction[-1] + cur > 0:
            cur += satisfaction.pop()
            ret += cur
        return ret