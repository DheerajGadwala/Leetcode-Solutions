class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        
        @cache
        def res(pos = 0):
            if pos == n:
                return 0
            else:
                w = shelf_width - books[pos][0]
                h = books[pos][1]
                ret = h + res(pos + 1)
                i = pos + 1
                while i < n and w - books[i][0] >= 0:
                    w -= books[i][0]
                    h = max(h, books[i][1])
                    ret = min(ret, h + res(i + 1))
                    i += 1
                return ret
            
        return res()
                    