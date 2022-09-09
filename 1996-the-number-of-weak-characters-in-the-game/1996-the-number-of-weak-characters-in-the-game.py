class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: [x[0], -x[1]])
        ret = 0
        mxdefence = -math.inf
        for i in range(len(properties)-1, -1, -1):
            mxdefence = max(mxdefence, properties[i][1])
            if mxdefence > properties[i][1]:
                ret += 1
        return ret
            