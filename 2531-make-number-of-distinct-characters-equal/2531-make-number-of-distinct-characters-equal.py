class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1 = dict()
        w2 = dict()
        for w in word1:
            if w not in w1:
                w1[w] = 0
            w1[w] += 1
        for w in word2:
            if w not in w2:
                w2[w] = 0
            w2[w] += 1
        
        for c1 in w1:
            for c2 in w2:
                if c1 == c2:
                    if len(w1) == len(w2):
                        return True
                    else:
                        continue
                l1 = len(w1) if w1[c1] > 1 else len(w1) - 1
                l2 = len(w2) if w2[c2] > 1 else len(w2) - 1
                ul1 = l1 if c2 in w1 else l1 + 1
                ul2 = l2 if c1 in w2 else l2 + 1
                if ul1 == ul2:
                    return True
        
        return False
                