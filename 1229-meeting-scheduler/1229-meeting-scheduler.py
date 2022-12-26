class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        while i < m and j < n:
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            if e1 <= s2:
                i += 1
            elif e2 <= s1:
                j += 1
            elif min(e1, e2) - max(s1, s2) >= duration:
                s = max(s1, s2)
                return [s, s + duration]
            elif e1 < e2:
                i += 1
            else:
                j += 1
        return []