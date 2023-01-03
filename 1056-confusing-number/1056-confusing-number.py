class Solution:
    def confusingNumber(self, n: int) -> bool:
        d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        n = str(n)
        rev = ''
        for i in n:
            if i not in d:
                return False
            else:
                rev = d[i] + rev
        return n != rev