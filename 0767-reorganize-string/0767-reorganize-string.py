class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = dict()
        for i in s:
            cnt[i] = cnt.get(i, 0) + 1
        l = [[-cnt[i], i] for i in cnt]
        heapify(l)
        x=heappop(l)
        ret = [x[1]]
        x[0] += 1
        if x[0] < 0:
            heappush(l, x)
        while len(l) > 0:
            if l[0][1] != ret[-1]:
                x = heappop(l)
                x[0] += 1
                ret.append(x[1])
                if x[0] < 0:
                    heappush(l, x)
            elif len(l) > 1:
                x = heappop(l)
                y = heappop(l)
                y[0] += 1
                ret.append(y[1])
                heappush(l, x)
                if y[0] < 0:
                    heappush(l, y)
            else:
                return ""
        return ''.join(ret)
                
            