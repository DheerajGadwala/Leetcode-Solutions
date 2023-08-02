class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        ret=[]
        l = [a, b, c]
        visited = [False, False, False]
        curr = ['', '', '']
        
        def merge(l):
            if len(l) == 0:
                return ''
            else:
                ret=l[0]
                for j in range(1, len(l)):
                    other = l[j]
                    new_ret = ret + other
                    for i in range(min(len(other), len(ret))):
                        x = len(other[:-1])
                        if other[:i+1] == ret[-1:-i-2:-1][::-1]:
                            new_ret = ret + other[i+1:]
                    ret = new_ret
                return ret
        
        
        def res(i = 0):
            if i == 3:
                ret.append(merge(curr))
            else:
                for j in range(3):
                    prev = curr[j]
                    curr[j] = l[i]
                    res(i+1)
                    curr[j] = prev
                res(i+1)

        res()
        l = []
        for i in ret:
            if a in i and b in i and c in i:
                l.append(i)
        l.sort(key = lambda x: (len(x), x))
        return l[0]