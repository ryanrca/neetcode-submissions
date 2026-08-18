class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, "head")
        self.tail = Node(-2, "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        self.capacity = capacity
        self.cache = {}
    
    def dump(self):
        cur = self.head
        print(f"{self.head.val} -> ", end="")
        while cur.next is not None:
            cur = cur.next
            if cur == self.tail:
                break
            print(f"{cur.val} -> ", end="")
        print(f"{self.tail.val}")


    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_front(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur = self.cache[key]
            cur.val = value
            self.move_to_front(cur)
            return

        n = Node(key, value)
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n

        self.head.next = n
        self.cache[key] = n
        self.count += 1
        self.trim_lru()

    def move_to_front(self, n: Node):

        n.prev.next = n.next
        n.next.prev = n.prev
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n

    def trim_lru(self):

        while self.count > self.capacity:

            cur = self.tail.prev

            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev

            del(self.cache[cur.key])
            del(cur)

            self.count -= 1
