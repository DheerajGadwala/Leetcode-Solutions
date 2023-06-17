class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        n = len(arr1)
        x = len(arr2)
        arr2.sort()
        
        def binary(val):
            l, h = 0, x - 1
            ans = -1
            while l <= h:
                m = (l + h) // 2
                if val >= arr2[m]:
                    l = m + 1
                else:
                    ans = m
                    h = m - 1
            if ans == -1:
                return ans
            elif arr2[ans] == val:
                return -1 if ans == x - 1 else ans + 1
            else:
                return ans
        
        @cache
        def res(pos = 0, prev = -1):
            if pos == n:
                return 0
            else:
                ret = math.inf if arr1[pos] <= prev else res(pos + 1, arr1[pos])
                best = binary(prev)
                if best != -1:
                    ret = min(ret, 1 + res(pos + 1, arr2[best]))
                return ret
            
        ans = res()
        
        return -1 if ans == math.inf else ans