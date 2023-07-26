class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        sm = 0
        groups = 0
        for i in usageLimits:
            sm += i
            if sm >= (groups+1) * (groups+2) // 2:
                groups += 1
        return groups