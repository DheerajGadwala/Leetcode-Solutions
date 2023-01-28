class SummaryRanges:

    def __init__(self):
        self.left = dict()
        self.right = dict()
        self.ret = set()
    
    def makeSet(self, u):
        self.left[u] = u
        self.right[u] = u
    
    def findLeft(self, u):
        if u not in self.left:
            self.makeSet(u)
            return u
        elif u == self.left[u]:
            return u
        else:
            self.left[u] = self.findLeft(self.left[u])
            return self.left[u]
    
    def findRight(self, u):
        if u not in self.right:
            self.makeSet(u)
            return u
        elif u == self.right[u]:
            return u
        else:
            self.right[u] = self.findRight(self.right[u])
            return self.right[u]
    
    def union(self, u):
        if u not in self.left:
            self.makeSet(u)
        ulp, urp = self.findLeft(u), self.findRight(u)
        rlp, rrp, llp, lrp = ulp, urp, ulp, urp
        if u + 1 in self.right:
            rlp, rrp = self.findLeft(u + 1), self.findRight(u + 1)
        if u - 1 in self.left:
            llp, lrp = self.findLeft(u - 1), self.findRight(u - 1)
        self.right[urp] = rrp
        self.right[lrp] = rrp
        self.left[ulp] = llp
        self.left[rlp] = llp
        li = (llp, lrp)
        mi = (ulp, urp)
        ri = (rlp, rrp)
        ni = (llp, rrp)
        self.ret.discard(li)
        self.ret.discard(mi)
        self.ret.discard(ri)
        self.ret.add(ni)
        

        

    def addNum(self, value: int) -> None:
        self.union(value)

    def getIntervals(self) -> List[List[int]]:
        ret = list(self.ret)
        ret.sort(key = lambda x: x[0])
        return ret


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()