class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        i = n
        need = 0
        a= 0
        cnt = 0
        prev = 1
        while i > 0:
            a += 1
            if prev < len(str(a)):
                i += cnt
            curr = 3 + 2*len(str(a))
            rem = limit - curr
            if rem <= 0:
                return []
            i -= rem
            need += limit
            prev = len(str(a))
            cnt += 1
        ret = []
        curr = []
        j = 1
        i = 0
        print(a)
        while i < len(message):
            excess = "<" + str(j) + "/" + str(a) + ">"
            rem = limit - len(excess)
            for k in range(rem):
                if i == len(message):
                    break
                curr.append(message[i])
                i += 1
            curr.append(excess)
            ret.append(''.join(curr))
            curr = []
            j += 1
        return ret
            