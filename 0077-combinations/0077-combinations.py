class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        l=[]
        def res(i = 1, k = k):
            nonlocal l
            if k == 0:
                ret.append(l[:])
                return
            elif i == n+1:
                return
            else:
                res(i+1, k)
                l.append(i)
                res(i+1, k-1)
                l.pop()
        res()
        return ret