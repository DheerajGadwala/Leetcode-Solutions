import heapq
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ptr = [0] * m
    
        def search(li, e):
            l, h = 0, len(li)-1
            while l <= h:
                m = (l + h) // 2
                if li[m] == e:
                    return True
                elif li[m] < e:
                    l = m + 1
                else:
                    h = m - 1
            return False
        
        for i in range(1, 10001):
            flag = True
            for l in mat:
                if not search(l, i):
                    flag = False
                    break
            if flag:
                return i
        
        return -1
                    