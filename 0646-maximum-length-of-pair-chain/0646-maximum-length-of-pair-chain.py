class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        currEnd = -1001
        ret = 0
        for x, y in pairs:
            if currEnd < x:
                currEnd = y
                ret += 1
        return ret