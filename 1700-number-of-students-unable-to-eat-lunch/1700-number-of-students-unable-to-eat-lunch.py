class Solution:
    def countStudents(self, st: List[int], sd: List[int]) -> int:
        
        n = len(st)
        
        stCnt = [0, 0]
        for i in range(n):
            stCnt[st[i]] += 1
            
        ans = 0
        while len(sd) > 0 and stCnt[sd[0]] != 0:
            if st[0] == sd[0]:
                stCnt[sd[0]] -= 1
                st.pop(0)
                sd.pop(0)
                ans += 1
            else:
                st.append(st.pop(0))
        
        return len(st)
        