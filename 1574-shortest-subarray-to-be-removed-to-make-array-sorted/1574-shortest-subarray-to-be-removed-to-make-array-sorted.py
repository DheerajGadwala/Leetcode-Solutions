class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [-math.inf] + arr + [math.inf]
        i, j = 0, len(arr) - 2
        n = len(arr)
        while i < n - 2:
            if arr[i + 1] >= arr[i]:
                i += 1
            else:
                break
        while j > i and arr[j] >= arr[i] and arr[j] <= arr[j+1]:
            j -= 1
        
        l = i + n - j
        while j > 0 and i > 0:
            i -= 1
            while j > i and arr[j] >= arr[i] and arr[j] <= arr[j+1]:
                j -= 1
            l = max(l, i + n - j)
        
        return n - l

            