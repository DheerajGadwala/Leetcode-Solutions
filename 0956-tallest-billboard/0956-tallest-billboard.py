class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        mem = {0:0}
        for i in rods:
            copy = dict(mem)
            for j in mem:
                diff, taller = j, mem[j]
                copy[diff + i] = max(taller + i, copy.get(diff + i, 0))
                if diff - i < 0:
                    copy[i - diff] = max(taller + i - diff, copy.get(i - diff, 0))
                else:
                    copy[diff - i] = max(taller, copy.get(diff - i, 0))
            mem = copy
        
        return mem[0]
        