class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars = 'qwertyuiopasdfghjklzxcvbnm'
        wf1, wf2 = {i:0 for i in chars}, {i:0 for i in chars}
        for w in word1:
            wf1[w] += 1
        for w in word2:
            wf2[w] += 1
        cf1, cf2 = dict(), dict()
        for c in chars:
            if wf1[c] not in cf1:
                cf1[wf1[c]] = 0
            cf1[wf1[c]] += 1
            if wf2[c] not in cf2:
                cf2[wf2[c]] = 0
            cf2[wf2[c]] += 1
        flag = True
        for f in cf1:
            flag &= f in cf2 and cf1[f] == cf2[f]
        for f in cf2:
            flag &= f in cf1 and cf1[f] == cf2[f]
        return flag and set(word1) == set(word2)
        