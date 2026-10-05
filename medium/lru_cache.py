class LRUCache:
    class node:
        def __init__(self, prev = None, next = None, val = 0, key = 0):
            self.prev = prev
            self.next = next
            self.val = val
            self.key = key

    def __init__(self, capacity: int):
        self.mapping = defaultdict(lambda: None)
        self.head = self.node(0, None, None, 0)
        self.tail = self.node(0, None, None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.nodeCount = 0

    def get(self, key: int) -> int:
        if key not in self.mapping.keys():
            return -1
        
        gotNode = self.mapping[key]
        gotNode.prev.next = gotNode.next
        gotNode.next.prev = gotNode.prev
        self.val_used(gotNode)
        return gotNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping.keys():
            self.del_node(key)
        elif self.nodeCount < self.capacity:
            self.nodeCount += 1
        else: 
            self.del_node(self.tail.prev.key)

        newNode = self.node(val = value, key = key)
        self.mapping[key] = newNode
        self.val_used(newNode)

    def del_node(self, key):
        n = self.mapping.pop(key)
        n.prev.next = n.next
        n.next.prev = n.prev
        del n

    def val_used(self, n):
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
