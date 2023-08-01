class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        @cache
        def res(n=n):
            ret=[]
            for i in range(2, math.floor(n**0.5+1)):
                if n % i == 0:
                    l = res(n//i)
                    r = res(i)
                    for j in l:
                        for k in r:
                            ret.append(j[:]+k[:])
            ret.append([n])
            for i in range(len(ret)):
                ret[i] = sorted(ret[i])
                ret[i] = tuple(ret[i])
            return set(ret)

        ans = list(res())
        ans.sort(key = lambda x: -len(x))
        ans.pop()
        return ans