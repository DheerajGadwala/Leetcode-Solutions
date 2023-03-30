class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        @cache
        def res(l1 = 0, h1 = n, l2 = 0, h2 = n):
            #print(l1, h1, l2, h2)
            if h2 == l2 + 1:
                return s1[l1] == s2[l2]
            ls1 = defaultdict(int)
            rs1 = defaultdict(int)
            ls2 = defaultdict(int)
            rs2 = defaultdict(int)
            for i in range(l1, h1):
                rs1[s1[i]] += 1
                ls1[s1[i]] = 0
            for i in range(l2, h2):
                rs2[s2[i]] += 1
                ls2[s2[i]] = 0
            ret = False
            #print("part1")
            for i in range(h2 - l2):
                ls1[s1[l1+i]] += 1
                ls2[s2[l2+i]] += 1
                rs1[s1[l1+i]] -= 1
                rs2[s2[l2+i]] -= 1
                #print(ls1, ls2, rs1, rs2)
                if ls1 == ls2 and rs1 == rs2 and i != h2 - l2 - 1:
                    ret |= res(l1, l1+i+1, l2, l2+i+1) and res(l1+i+1, h1, l2+i+1, h2) 
            ls1, rs1 = rs1, ls1
            #print("part2")
            for i in range(h2 - l2 - 1):
                ls1[s1[l1+i]] += 1
                rs2[s2[h2-i-1]] += 1
                rs1[s1[l1+i]] -= 1
                ls2[s2[h2-i-1]] -= 1
                #print(ls1, rs2, ls2, rs1)
                if ls1 == rs2 and ls2 == rs1 and i != h2 - l2 - 1:
                    ret |= res(l1, l1+i+1, h2-i-1, h2) and res(l1+i+1, h1, l2, h2-i-1)
            ls2, rs2 = rs2, ls2
            return ret
        return res()
                