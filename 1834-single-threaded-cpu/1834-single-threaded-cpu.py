class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q = []
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(len(tasks))]
        tasks.sort(key = lambda x: x[0])
        t = tasks[0][0]
        j = 0
        
        class Task:
            def __init__(self, e, p, i):
                self.e = e
                self.p = p
                self.i = i
            
            def __lt__(self, other):
                if self.p == other.p:
                    return self.i < other.i
                else:
                    return self.p < other.p
        
        ret = []
        while j < len(tasks) or len(q) > 0:
            while j < len(tasks) and tasks[j][0] <= t:
                heappush(q, Task(tasks[j][0], tasks[j][1], tasks[j][2]))
                j += 1
            if len(q) == 0:
                t = tasks[j][0]
                continue
            done = heappop(q)
            t += done.p
            ret.append(done.i)
        
        return ret