class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        sec = 0
        curr = s
        while True:
            cnt = 0
            i = 1
            while i < len(s):
                if s[i-1] == '0' and s[i] == '1':
                    s[i-1], s[i] = s[i], s[i-1]
                    i += 2
                    cnt += 1
                else:
                    i += 1
            if (cnt == 0):
                break
            else:
                sec += 1
        return sec