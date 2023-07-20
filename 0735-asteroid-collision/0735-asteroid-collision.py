class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        r, l = [], []
        for i in asteroids:
            if i > 0:
                r.append(i)
            else:
                while len(r) > 0 and r[-1] < -i:
                    r.pop()
                if len(r) == 0:
                    l.append(i)
                elif r[-1] == -i:
                    r.pop()
        return l + r
            