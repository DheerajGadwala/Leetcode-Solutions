class Solution:
    def partition(self, k: str) -> List[List[str]]:
        
        
        def isPal(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        @cache
        def res(s = k):
            if s == "":
                return [[]]
            n = len(s)
            curr = ""
            ret = []
            for i in range(n):
                curr += s[i]
                if (isPal(curr)):
                    rem = res(s[i+1:])
                    for val in rem:
                        ret.append([curr] + val)
            return ret
        
        return res()
                    