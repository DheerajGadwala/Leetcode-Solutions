class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        i = 1
        mp = dict()
        all_skills = 0
        for j in req_skills:
            mp[j] = i
            all_skills |= i
            i <<= 1
            
        mem = dict()
        trace = dict()
        
        def res(pos = 0, mask = 0):
            if (pos, mask) in mem:
                return mem[(pos, mask)]
            elif mask == all_skills:
                return 0
            elif pos == n:
                return math.inf
            else:
                nxt_mask = mask
                for j in people[pos]:
                    if j in mp:
                        nxt_mask |= mp[j]
                a = res(pos+1, mask)
                b = 1 + res(pos + 1, nxt_mask)
                if a < b:
                    trace[(pos, mask)] = (pos+1, mask)
                    mem[(pos, mask)] = a
                else:
                    trace[(pos, mask)] = (pos+1, nxt_mask)
                    mem[(pos, mask)] = b
                return mem[(pos, mask)]

        ans = res()

        k = (0, 0)
        ret = []
        while k in trace:
            if k[1] != trace[k][1]:
                ret.append(k[0])
            k = trace[k]
        return ret