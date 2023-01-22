class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        a, b = targetX, targetY
        while a != 1 or b != 1:
            if a % 2 == 0:
                a //= 2
            elif b % 2 == 0:
                b //= 2
            elif a > b:
                a += b
            elif a < b:
                b += a
            else:
                return False
        return True