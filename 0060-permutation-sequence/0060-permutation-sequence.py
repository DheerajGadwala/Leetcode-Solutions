class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, n+1):
            fact.append(fact[-1]*i)
        ret = []
        l = [i for i in range(1, n+1)]
        k-=1
        while n != 0:
            n-=1
            ret.append(str(l[k//fact[n]]))
            del l[k//fact[n]]
            k %= fact[n]
        return ''.join(ret)
        
                        