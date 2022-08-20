class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = list(s)
        s = [0] * len(l)
        e = [0] * len(l)
        for i in shifts:
            if i[2] == 1:
                s[i[0]] += 1
                e[i[1]] += 1
            else:
                s[i[0]] -= 1
                e[i[1]] -= 1
                
        for i in range(len(l) - 2, -1, -1):
            s[i] += s[i+1]
            e[i] += e[i+1]
        
        for i in range(len(l) - 1):
            e[i] -= s[i + 1]
            
        for i in range(len(l)):
            c = ord(l[i]) - ord('a')
            c = (c + e[i]) % 26
            c += ord('a')
            l[i] = chr(c)
        return ''.join(l)
                