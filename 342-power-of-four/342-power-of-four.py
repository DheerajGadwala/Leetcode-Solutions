class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log(n, 4) - round(math.log(n, 4)) == 0