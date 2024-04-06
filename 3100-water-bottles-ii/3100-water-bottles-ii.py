class Solution:
    def maxBottlesDrunk(self, n: int, x: int) -> int:
        ans = 0
        while n >= x:
            ans += x
            n -= x - 1
            x += 1
        return ans + n
