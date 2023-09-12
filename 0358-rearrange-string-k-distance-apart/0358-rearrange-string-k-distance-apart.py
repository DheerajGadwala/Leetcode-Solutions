class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        cnt = {i:0 for i in set(s)}
        for i in s:
            cnt[i] += 1
        x = [[i, cnt[i]] for i in cnt]
        x.sort(key = lambda x: -x[1])
        l = []
        i = 0
        while len(x) > 0:
            l.append(x[i][0])
            x[i][1] -= 1
            i += 1
            i %= min(k, len(x))
            if i == 0:
                x.sort(key = lambda x:-x[1])
                while len(x) > 0 and x[-1][-1] == 0:
                    x.pop()
        prev = dict()
        for i in range(len(l)):
            if l[i] not in prev:
                prev[l[i]] = i
            else:
                if i - prev[l[i]] < k:
                    return ""
                prev[l[i]] = i
        return ''.join(l)
            