class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, n):
                a = int(num[:i])
                if len(num[i:j]) > 1 and num[i] == '0':
                    continue
                b = int(num[i:j])
                pos = j
                while pos < n:
                    c = ''
                    while c == '' or (int(c) < a + b and pos < n):
                        c += num[pos]
                        pos += 1
                    if len(c) > 1 and c[0] == '0':
                        break
                    if int(c) == a + b:
                        if pos == n:
                            return True
                        a = b
                        b = int(c)
                    else:
                        break
        return False
                        