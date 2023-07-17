class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        k = 2
        events.sort(key = lambda x: x[0])
        n = len(events)

        def search(tar):
            l, h = 0, n - 1
            ret = None
            while l <= h:
                m = (l + h) // 2
                if events[m][0] < tar:
                    l = m + 1
                else:
                    ret = m
                    h = m - 1
            return ret
        
        @cache
        def res(pos = 0, k = k):
            if pos == None or pos == n or k == 0:
                return 0
            else:
                return max(events[pos][2] + res(search(events[pos][1]+1), k-1), res(pos + 1, k))
        
        return res()