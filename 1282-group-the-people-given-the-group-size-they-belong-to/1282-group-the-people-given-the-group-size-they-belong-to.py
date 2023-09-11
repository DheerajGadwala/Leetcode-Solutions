class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict()
        ret = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = [i]
            else:
                d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]]) == groupSizes[i]:
                ret.append(d.pop(groupSizes[i]))
        return ret