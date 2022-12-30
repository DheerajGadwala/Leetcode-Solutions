# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:
        r, c = bm.dimensions() 
        ans = math.inf
        
        for i in range(r):
            
            l, h = 0, c - 1
            floor = math.inf
            while l <= h:
                
                m = (l + h) // 2
                
                val = bm.get(i, m)
                
                if val == 0:
                    l = m + 1
                    
                else:
                    floor = m
                    h = m - 1
            
            ans = min(ans, floor)
        
        return -1 if ans == math.inf else ans
        
        