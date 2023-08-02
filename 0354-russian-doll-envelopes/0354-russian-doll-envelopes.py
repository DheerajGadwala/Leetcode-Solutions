class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        
        e.sort(key = lambda x: (x[0], -x[1]))
        lis = [e[0]]
        
        def search(tar):
            n = len(lis)
            l, h = 0, n-1
            ret = n
            while l<=h:
                m = (l+h)//2
                if lis[m][1]>=tar:
                    ret=m
                    h=m-1
                else:
                    l=m+1
            return ret
        
        for i in range(1, len(e)):
            if e[i][1] > lis[-1][1]:
                lis.append(e[i])
            else:
                lis[search(e[i][1])] = e[i]

        return len(lis)
            
            
                
            
                