class Solution:
    def minFlips(self, s: str) -> int:
        oz, oo, ez, eo = 0, 0, 0, 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if i % 2 == 0:
                if c == '0':
                    ez += 1
                else:
                    eo += 1
            else:
                if c == '0':
                    oz += 1
                else:
                    oo += 1
        
        ans = min(ez + oo, eo + oz)
        
        for i in range(n):
            eo, oo = oo, eo
            ez, oz = oz, ez
            if n % 2 == 1:
                c = s[i]
                if c == '0':
                    oz -= 1
                    ez += 1
                else:
                    oo -= 1
                    eo += 1
            ans = min(ans, min(ez + oo, eo + oz))
            # print(oz, oo, ez, eo)
        
        return ans
            
        