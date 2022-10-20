class Solution:
    def intToRoman(self, num: int) -> str:
        
        def getRoman(n, a, b, c):
            if n < 4:
                return n*a
            elif n == 4:
                return a + b
            elif n == 5:
                return b
            elif n < 9:
                return b + ((n - 5) * a)
            else:
                return a + c
        
        ret = ""
        l = ["I", "V", "X", "L", "C", "D", "M", "", ""]
        i = 0
        while num > 0:
            n = num%10
            num = num//10
            ret = getRoman(n, l[i], l[i+1], l[i+2]) + ret
            i += 2
        return ret