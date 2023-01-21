class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ret = []
        
        isValid = lambda x: (len(x) == 1 or (len(x) > 1 and x[0] != '0')) and int(x) <= 255 
        
        for i in range(n):
            for j in range(i+1 , n):
                for k in range(j+1, n):
                    w, x, y, z = s[:i], s[i:j], s[j:k], s[k:]
                    if isValid(w) and isValid(x) and isValid(y) and isValid(z):
                        ret.append(w+'.'+x+'.'+y+'.'+z)
        
        return ret
                    