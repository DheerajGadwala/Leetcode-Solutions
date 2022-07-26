class Solution:
    def stoneGameIII(self, s: List[int]) -> str:
        
        @cache
        def res(pos = 0):
            if pos == len(s):
                return 0
            else:
                a = s[pos] - res(pos + 1)
                b = -math.inf if pos + 1 >= len(s) else s[pos] + s[pos + 1] - res(pos + 2)
                c = -math.inf if pos + 2 >= len(s) else s[pos] + s[pos + 1] + s[pos + 2] - res(pos + 3)
                return max(a, b, c)
        ans = res()
        return "Bob" if ans < 0 else "Alice" if ans > 0 else "Tie"