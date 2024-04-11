class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        def res(l=deck):
            if len(l) == 1:
                return l[:]
            x, y = l[:math.ceil(len(l)/2)], l[math.ceil(len(l)/2):]
            y_ = res(y)
            ret = []
            flg = True
            if len(x) > len(y):
                y_.insert(0, y_.pop())
            while len(x) != 0 or len(y_) != 0:
                if flg:
                    ret.append(x.pop(0))
                else:
                    ret.append(y_.pop(0))
                flg = not flg
            return ret
        
        return res()
    
    
    
    
    
    
    