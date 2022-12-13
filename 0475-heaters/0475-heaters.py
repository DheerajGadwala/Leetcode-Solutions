class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        m, n = len(houses), len(heaters)
        def search(val):
            l, h = 0, n - 1
            floor, ceil = 0, n-1
            while l <= h:
                mid = (l + h) // 2
                if heaters[mid] == val:
                    return mid, mid
                elif heaters[mid] < val:
                    floor = mid
                    l = mid + 1
                else:
                    ceil = mid
                    h = mid - 1
            return floor, ceil
        
        radius = 0
        
        for i in houses:
            f, c = search(i)
            radius = max(radius, min(abs(i - heaters[f]), abs(i - heaters[c])))
            
        return radius
        