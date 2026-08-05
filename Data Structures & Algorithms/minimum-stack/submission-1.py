class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class MinStack:

    def __init__(self):
        self.count = 0
        self.minval = None
        self.tail = None
        
    def dump(self):
        cur = self.tail
        while cur is not None:
            print(f" [{cur.val}] -> ", end="")
            cur = cur.prev
        print(f"\n min: {self.minval} - count: {self.count}")


    def push(self, val: int) -> None:

        new_node = Node(val)

        if self.count == 0:
            self.tail = new_node
            self.minval = val
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.minval = min(self.minval, val)
        self.count += 1
        
    def _recalc_min(self):

        cur = self.tail
        self.minval = cur.val

        if self.count == 0:
            self.minval = None
            return

        while cur != None:
            self.minval = min(self.minval, cur.val)
            cur = cur.prev

    def pop(self) -> None:
        if self.count == 0:
            return
        if self.count == 1:
            self.tail = None
            self.count -= 1
            self.minval = None
            return
        tmp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1

        if tmp.val == self.minval:
            self._recalc_min()

        return 
        

    def top(self) -> int:
        if not self.tail:
            return None
        return self.tail.val
        

    def getMin(self) -> int:
        return self.minval
        