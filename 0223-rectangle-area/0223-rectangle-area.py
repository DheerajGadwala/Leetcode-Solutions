class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int,bx2: int, by2: int) -> int:
        a1 = (ax2-ax1)*(ay2-ay1)
        a2 = (bx2-bx1)*(by2-by1)
        
        x_o = - max(bx1, ax1) + min(bx2, ax2)
        y_o = - max(by1, ay1) + min(by2, ay2)
        
        if x_o > 0 and y_o > 0:
            return a1 + a2 - x_o*y_o
        else:
            return a1 + a2
        
        