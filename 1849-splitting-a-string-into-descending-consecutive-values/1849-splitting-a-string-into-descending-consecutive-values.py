class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        prev = ""
        ans = False
        
        def res(pos, prev):
            if pos == len(s):
                return len(s) != len(prev)
            curr = ""
            ret = False
            for i in range(pos, n):
                curr += s[i]
                if int(curr) + 1 == int(prev):
                    ret |= res(i + 1, curr)
            return ret
        
        for i in range(n):
            prev += s[i]
            ans |= res(i+1, prev)
        return ans
        
        
        