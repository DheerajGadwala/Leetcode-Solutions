class Solution:
    def expand(self, s: str) -> List[str]:
        n = len(s)
        l = []
        i = 0
        while i < n:
            if s[i] == '{':
                i += 1
                x = []
                while s[i] != '}':
                    if s[i] != ',':
                        x.append(s[i])
                    i += 1
                i += 1
                x.sort()
                l.append(x)
            else:
                l.append([s[i]])
                i += 1
        
        n = len(l)
        ret = []
        def res(pos = 0, acc = ''):
            if pos == n:
                ret.append(acc)
            else:
                for elem in l[pos]:
                    res(pos + 1, acc + elem)
        res()
        return ret
                        
            