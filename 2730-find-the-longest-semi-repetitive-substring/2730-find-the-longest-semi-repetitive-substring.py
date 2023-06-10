class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        x = deque([])
        rep = False
        ans = 0
        for i in s:
            if len(x) < 1:
                x.append(i)
            elif i == x[-1] and not rep:
                x.append(i)
                rep = True
            elif i == x[-1] and rep:
                while x[0] != x[1]:
                    x.popleft()
                x.popleft()
                rep = i == x[-1]
                x.append(i)
            else:
                x.append(i)
            #print(x)
            ans = max(ans, len(x))
        return ans