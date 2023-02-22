class Solution:
    def assignTasks(self, s: List[int], t: List[int]) -> List[int]:
        m , n = len(s), len(t)
        ret = [None] * n
        s = [(s[i], i) for i in range(m)]
        heapify(s)
        running = []
        q = []
        time = 0
        while time < n:
            q.append((t[time], time))
            while len(running) != 0 and running[0][0] == time:
                heappush(s, heappop(running)[1])
            while len(s) != 0 and len(q) != 0:
                x = heappop(s)
                y = q.pop(0)
                heappush(running, (time+y[0], x))
                ret[y[1]] = x[1]
            time += 1
        #print(q, running, time)
        while len(q) != 0:
            while len(running) != 0 and running[0][0] == time:
                heappush(s, heappop(running)[1])
            while len(s) != 0 and len(q) != 0:
                x = heappop(s)
                y = q.pop(0)
                heappush(running, (time+y[0], x))
                ret[y[1]] = x[1]
            time = running[0][0]
        return ret
            