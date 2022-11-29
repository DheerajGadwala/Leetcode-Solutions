class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lostNone = set()
        lostOne = set()
        lostMore = set()
        for w, l in matches:
            if l in lostNone:
                lostNone.remove(l)
                lostOne.add(l)
            elif l in lostOne:
                lostOne.remove(l)
                lostMore.add(l)
            elif l not in lostNone and l not in lostMore:
                lostOne.add(l)
            if w not in lostOne and w not in lostMore:
                lostNone.add(w)
            # print((w, l), lostNone, lostOne, lostMore)
        return [sorted(lostNone), sorted(lostOne)]
                