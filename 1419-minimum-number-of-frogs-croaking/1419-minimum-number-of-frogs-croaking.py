class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {i:0 for i in 'croak'}
        prev = {'r':'c', 'o':'r', 'a':'o', 'k':'a'}
        ret = 0
        n = len(croakOfFrogs)
        for i in range(n):
            c = croakOfFrogs[i]
            if c != 'c':
                d[prev[c]] -= 1
                if d[prev[c]] < 0:
                    return -1
            d[c] += 1
            flag = True
            for c in 'croa':
                flag &= d[c] == 0
            d['k'] = 0
            ret = max(ret, sum(d.values()))
        for c in 'croa':
            if d[c] != 0:
                return -1
        return max(ret, d['k'])