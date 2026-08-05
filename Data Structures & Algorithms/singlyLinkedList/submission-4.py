class Node:
    def __init__(self, val=None):
        self.val =val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if self.head == None or index >= self.size:
            return -1
        count = 0
        cursor = self.head
        while count < index:
            cursor = cursor.next
            count += 1
        return cursor.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        self.size += 1

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.size == 0:
            self.head = node
            self.size += 1
            return

        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if self.size == 0:
            return False
        if index >= self.size:
            return False

        if index == 0:
            remove_node = self.head
            self.head = self.head.next
            del(remove_node)
            self.size -= 1
            return True

        count = 0
        cursor = self.head
        while count < index - 1:
            cursor = cursor.next
            count += 1

        remove_node = cursor.next
        cursor.next = remove_node.next
        del(remove_node)

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        cursor = self.head
        ret = []
        while cursor:
            ret.append(cursor.val)
            cursor = cursor.next
        return ret
