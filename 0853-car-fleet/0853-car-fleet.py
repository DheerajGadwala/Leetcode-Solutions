class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        sp = [(speed[i], position[i]) for i in range(n)]
        sp.sort(key = lambda x: x[1])
        ans = 1
        while len(sp) > 1:
            s1, p1 = sp.pop()
            s2, p2 = sp.pop()
            t = math.inf if s1 >= s2 else (p1 - p2) / (s2 - s1)
            if s1 * t + p1 > target:
                sp.append((s2, p2))
                ans += 1
            elif s1 < s2:
                sp.append((s1, p1))
            elif s1 >= s2:
                sp.append((s2, p2))
        return ans