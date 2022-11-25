class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        def strob(n):
            ret = ''
            for i in str(n)[::-1]:
                if i in '180':
                    ret += i
                elif i == '6':
                    ret += '9'
                elif i == '9':
                    ret += '6'
                else:
                    return None
            return ret
        
        return str(num) == strob(num)