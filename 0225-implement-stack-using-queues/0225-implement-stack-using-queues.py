class MyStack:

    def __init__(self):
        self.a = deque([])
        self.b = deque([])

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        while len(self.a) > 1:
            self.b.append(self.a.popleft())
        self.b, self.a = self.a, self.b
        return self.b.popleft()

    def top(self) -> int:
        while len(self.a) > 1:
            self.b.append(self.a.popleft())
        ret = self.a.popleft()
        self.b.append(ret)
        self.a, self.b = self.b, self.a
        return ret 

    def empty(self) -> bool:
        return len(self.a) + len(self.b) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()