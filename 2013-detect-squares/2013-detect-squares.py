class DetectSquares:

    def __init__(self):
        self.ps = dict()

    def add(self, point: List[int]) -> None:
        point = (point[0], point[1])
        if point not in self.ps:
            self.ps[point] = 0
        self.ps[point] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for x, y in self.ps:
            if point[0] == x and point[1] != y:
                ly, sy = max(point[1], y), min(point[1], y)
                s = ly - sy
                a = (x + s, sy)
                b = (x + s, ly)
                c = (x, y)
                if a in self.ps and b in self.ps:
                    ans += self.ps[a] * self.ps[b] * self.ps[c]
                a = (x - s, sy)
                b = (x - s, ly)
                if a in self.ps and b in self.ps:
                    ans += self.ps[a] * self.ps[b] * self.ps[c]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)