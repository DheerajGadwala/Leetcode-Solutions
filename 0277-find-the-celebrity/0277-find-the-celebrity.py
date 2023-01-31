# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        eliminated = set()
        i, j = 0, 1
        while i < n and j < n:
            if knows(i, j):
                eliminated.add(i)
                i = max(i, j) + 1
            else:
                eliminated.add(j)
                j = max(i, j) + 1
        i = min(i, j)
        isCelb = True
        for k in range(n):
            isCelb &= k == i or (knows(k, i) and not knows(i, k))
        return i if isCelb else -1