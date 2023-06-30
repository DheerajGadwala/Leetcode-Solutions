class DisjointSets:
    
    def __init__(self):
        self.right = dict()
        self.left = dict()
    
    
    
    def findRight(self, u):
        if u not in self.right or self.right[u] == u:
            self.right[u] = u
            return u
        else:
            self.right[u] = self.findRight(self.right[u])
            return self.right[u]

    def findLeft(self, u):
        if u not in self.left or self.left[u] == u:
            self.left[u] = u
            return u
        else:
            self.left[u] = self.findLeft(self.left[u])
            return self.left[u]
    
    def union(self, u):
        l, r = math.inf, -math.inf
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    uParRight = self.findRight(u)
                    uParLeft = self.findLeft(u)
                    v = (u[0] + i, u[1] + j)
                    if v in self.right:
                        vParRight = self.findRight(v)
                        if vParRight[1] < uParRight[1]:
                            self.right[vParRight] = uParRight
                        elif vParRight[1] == uParRight[1]:
                            if vParRight[0] < uParRight[0]:
                                self.right[vParRight] = uParRight
                            else:
                                self.right[uParRight] = vParRight
                        else:
                            self.right[uParRight] = vParRight
                        r = max(r, self.findRight(u)[1])
                    if v in self.left:
                        vParLeft = self.findLeft(v)
                        if vParLeft[1] < uParLeft[1]:
                            self.left[uParLeft] = vParLeft
                        elif vParLeft[1] == uParLeft[1]:
                            if vParLeft[0] < uParLeft[0]:
                                self.left[vParLeft] = uParLeft
                            else:
                                self.left[uParLeft] = vParLeft
                        else:
                            self.left[vParLeft] = uParLeft
                        l = min(l, self.findLeft(u)[1])
        return l, r
        

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        ds = DisjointSets()
        days = 0
        for cell in cells:
            l, r = ds.union(tuple(cell))
            if l == 1 and r == col:
                return days
            days += 1
        return 0