class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        
        regular = regular[::-1]
        express = express[::-1]
        n = len(regular)
        
        @cache
        def res(pos = 0, e = False):
            if pos == n:
                return 0
            elif not e:
                return min(regular[pos] + res(pos+1), expressCost + express[pos] + res(pos+1, True))
            else:
                return min(express[pos] + res(pos+1, True), regular[pos] + res(pos+1))
            
        return [res(i) for i in range(n-1,-1,-1)]