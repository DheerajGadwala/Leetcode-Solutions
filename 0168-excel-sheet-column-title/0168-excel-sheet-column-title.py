class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = []
        while n > 0:
            n -= 1
            ret.insert(0, chr(n % 26 + ord('A')))
            n //= 26
        return ''.join(ret)