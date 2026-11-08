
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:

        if self.size == 0:
            node = Node(value)
            self.head = node
            self.tail = node
            self.size += 1
            return
        
        node = Node(value)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1
        return

    def appendleft(self, value: int) -> None:

        if self.size == 0:
            node = Node(value)
            self.head = node
            self.tail = node
            self.size += 1
            return

        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return

    def pop(self) -> int:
        if self.size == 0:
            return -1
        if self.size == 1:
            cur = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return cur.value

        ret = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return ret

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        if self.size == 1:
            cur = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return cur.value
        
        ret = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return ret
