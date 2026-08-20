class LRUCache:
    class Node:
        def __init__(self, key = 0, val = 0, next = None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev
            self.key = key
        
    def __init__(self, capacity: int):
        self.d = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1, prev = self.head)
        self.head.next = self.tail
        self.cnt = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.d.get(key, None) == None:
            return -1
        node = self.d[key]
        ans = node.val
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        return ans
        

    def put(self, key: int, value: int) -> None:
        if self.d.get(key, None) == None:
            if self.cnt < self.capacity:
                self.cnt += 1
            else:
                todel = self.head.next
                self.head.next = todel.next
                todel.next.prev = self.head
                del self.d[todel.key]

            node = self.Node(key = key, val = value)
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            self.d[key] = node
        else:
            node = self.d[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            
