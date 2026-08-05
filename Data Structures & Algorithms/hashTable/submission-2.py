'''
The solution is to make an array of link-lists.
The key will be hashed simply: (key % capacity) to return an index for the array.
insert, del and resize are the complex methods, the rest are simple.
'''

class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.val = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.usage = 0
        self.table = [None] * self.capacity

    def hash_index(self, key: int) -> int:
        return key % self.capacity

    def check_capacity(self):
        load = self.capacity//2
        if self.usage >= load:
            self.resize()

    def dump_ll(self):
        for i in range(len(self.table)):
            node = self.table[i]
            if node:
                while node.next:
                    print(f"-{i}- node: [{node.key}] : {node.val} -> ", end="")
                    node = node.next
            else:
                print(f"-{i}- empty")
                continue
            print(f"-{i}- node: [{node.key}] : {node.val}")
        

    def insert(self, key: int, value: int) -> None:
        index = self.hash_index(key)

        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            node = self.table[index]
            while node:
                if node.key == key:
                    node.val = value
                    return
                else:
                    prev, node = node, node.next

            node = Node(key, value)
            prev.next = node

        self.usage += 1
        self.check_capacity()
            
    def get(self, key: int) -> int:
        index = self.hash_index(key)
        if not self.table[index]:
            return -1

        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_index(key)
        node = self.table[index]
        if not node:
            return False
        if node.key == key:
            self.table[index] = node.next
            self.usage -= 1
            return True

        while node.next:
            prev, node = node, node.next
            if node.key == key:
                prev.next = node.next
                self.usage -= 1
                return True
        return False


    def getSize(self) -> int:
        return self.usage

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_table = [None] * self.capacity

        for n in self.table:
            if not n:
                continue

            cursor = n
            index = self.hash_index(cursor.key)

            if not new_table[index]:
                new_table[index] = Node(cursor.key, cursor.val)

            else:
                new = Node(cursor.key, cursor.val)
                new.next = new_table[index]
                new_table[index] = new

        self.table = new_table.copy()


