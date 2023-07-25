class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = (l+h)//2
            if m > 0 and m < len(arr)-1 and arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m
            elif m == 0 and arr[m] > arr[m+1]:
                return m
            elif m == len(arr) - 1 and arr[m] > arr[m-1]:
                return m
            elif m == 0 or arr[m] > arr[m-1]:
                l = m + 1
            else:
                h = m - 1