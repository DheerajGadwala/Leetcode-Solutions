class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        if len(s2) > len(s1):
            return False
        ms2 = dict()
        for i in s2:
            if i in ms2:
                ms2[i] += 1
            else:
                ms2[i] = 1
        ms1 = dict()
        for i in range(len(s2)):
            if s1[i] in ms1:
                ms1[s1[i]] += 1
            else:
                ms1[s1[i]] = 1
        def check():
            for i in ms1:
                if i in ms2 and ms1[i] == ms2[i]:
                    continue
                else:
                    return False
            return True
        if check():
            return True
        for i in range(len(s2), len(s1)):
            ms1[s1[i-len(s2)]] -= 1
            if ms1[s1[i-len(s2)]] == 0:
                del ms1[s1[i-len(s2)]]
            if s1[i] in ms1:
                ms1[s1[i]] += 1
            else:
                ms1[s1[i]] = 1
            if check():
                return True
        return False