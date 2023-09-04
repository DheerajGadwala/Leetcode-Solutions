class TwoSum:

    def __init__(self):
        self.mp = dict()

    def add(self, number: int) -> None:
        self.mp[number] = self.mp.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for i in self.mp:
            j = value - i
            if i != j and j in self.mp:
                return True
            elif i == j and self.mp[i] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)