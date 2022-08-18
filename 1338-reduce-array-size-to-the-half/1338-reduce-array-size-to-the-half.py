class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = dict()
        for i in arr:
            cnt[i] = 1 if i not in cnt else cnt[i] + 1
        l = list(cnt.values())
        tar = sum(l) / 2
        l.sort(key = lambda x: -x)
        sm = 0
        i = 0
        while sm < tar:
            sm += l[i]
            i += 1
        return i
            
        