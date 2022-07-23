class Node:
    
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ret = self.cache[key].val
        self.update(key, ret)
        return ret

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.insert(key, value)
            if len(self.cache) == self.capacity + 1:
                self.remove()
        else:
            self.update(key, value)
                
    def insert(self, key, value):
        node = Node(value, key)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.cache[key] = node
    
    def remove(self):
        k = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        del self.cache[k.key]
    
    def update(self, key, value):
        k = self.cache[key]
        k.val = value
        k.prev.next = k.next
        k.next.prev = k.prev
        k.next = self.head.next
        self.head.next.prev = k
        k.prev = self.head
        self.head.next = k
        self.cache[key] = k


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)