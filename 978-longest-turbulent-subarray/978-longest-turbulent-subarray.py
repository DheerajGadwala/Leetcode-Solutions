class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        mx = 1
        curr = 1
        inc = False
        dec = False
        for i in range(1, len(arr)):
            if inc:
                if arr[i] < arr[i-1]:
                    inc, dec = False, True
                    curr += 1
                elif arr[i] == arr[i-1]:
                    inc, dec = False, False
                    curr = 1
                else:
                    inc, dec = True, False
                    curr = 2
            elif dec:
                if arr[i] > arr[i-1]:
                    inc, dec = True, False
                    curr += 1
                elif arr[i] == arr[i-1]:
                    inc, dec = False, False
                    curr = 1
                else:
                    inc, dec = False, True
                    curr = 2
            else:
                inc = arr[i] > arr[i-1]
                dec = arr[i] < arr[i-1]
                if inc or dec:
                    curr = 2
                else:
                    curr = 1
            mx = max(mx, curr)
        return mx
            
                
            