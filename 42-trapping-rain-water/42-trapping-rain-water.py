class Solution:
    def trap(self, h: List[int]) -> int:
        # preprocessing
        # removing incline from the beginning
        while len(h) > 1 and h[1] >= h[0]:
            h.pop(0)
        # removing descent from the ending
        while len(h) > 1 and h[-1] <= h[-2]:
            h.pop()
        # monotonic stack
        s = [(h[0], 1)]
        amt = 0
        for i in range(1, len(h)):
            length = 1
            while len(s) > 0 and h[i] > s[-1][0]:
                waterHeight = min(h[i], s[0][0]) # collect water upto this height
                ht, nt = s.pop() # height of popped floor, length of popped floor
                amt += (waterHeight - ht) * nt # area of water added
                length += nt # length of current floor with height h[i]
            s.append((h[i], length)) # add floor with height h[i] and length 
        
        return amt
        