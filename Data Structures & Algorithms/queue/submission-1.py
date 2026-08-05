class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def isEmpty(self) -> bool:
        return self.count == 0

    def append(self, value: int) -> None:

        node = Node(value)

        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def appendleft(self, value: int) -> None:
        node = Node(value)

        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            return -1
        if self.count == 1:
            cursor = self.tail
            self.head = None
            self.tail = None
            self.count -= 1
            return cursor.val

        cursor = self.tail

        print(f"POP: {self.count} {cursor.val}")

        cursor.prev.next = None
        self.tail = cursor.prev
        self.count -= 1
        return cursor.val

    def popleft(self) -> int:
        if self.count == 0:
            return -1
        if self.count == 1:
            cursor = self.head
            self.head = None
            self.tail = None
            self.count -= 1
            return cursor.val



        cursor = self.head
        self.head = cursor.next
        cursor.next = None
        self.count -= 1
        return cursor.val


