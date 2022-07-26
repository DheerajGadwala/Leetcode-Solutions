class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        mx = 1
        curr = 1
        inc = False
        dec = False
        for i in range(1, len(arr)):
            nextInc = arr[i] > arr[i-1]
            nextDec = arr[i] < arr[i-1]
            if (inc and nextDec) or (dec and nextInc):
                curr += 1
            elif nextInc or nextDec:
                curr = 2
            else:
                curr = 1
            inc = nextInc
            dec = nextDec
            mx = max(mx, curr)
        return mx
            
                
            